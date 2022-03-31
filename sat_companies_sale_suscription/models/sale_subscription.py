# -*- coding: utf-8 -*-
from markupsafe import string
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import datetime
from pytz import timezone
import base64
import logging


class SaleSuscriptionInherit(models.Model):
    _inherit = 'sale.subscription'

    active_cron_invoice = fields.Boolean(
        string="Active cron")
    gadget_contract_type = fields.Many2one(
        'stock.gadgets.contract.type',
        string="Contract type")
    is_potential_client = fields.Boolean(
        string="Is a potential client",
        tracking=True,
        related="partner_id.is_potential_client")
    product_id = fields.Many2one(
        'product.template',
        'Gadgets')
    task_user_id = fields.Many2one(
        'res.users')
    sale_type_id = fields.Many2one(
        'sale.order.type')
    gadgest_contract_type_id = fields.Many2one(
        'stock.gadgets.contract.type')
    date_begin = fields.Datetime(
        string = 'Date asigned')
    date_end = fields.Datetime(
        string = 'Date End asingned')
    check_contract_type = fields.Boolean(
        compute="_compute_check_contract_type",
        )
    signature = fields.Image(
        'Signature',
        help='Signature received through the portal.',
        copy=False,
        attachment=True,
        max_width=1024,
        max_height=1024)
    signed_by = fields.Char(
        'Signed By',
        help='Name of the person that signed the SO.',
        copy=False)
    signed_on = fields.Datetime(
        'Signed On',
        help='Date of the signature.',
        copy=False)
    pdf_file_sale_contract = fields.Binary(
        'PDF Contrato',
        attachment=True)
    is_extension = fields.Boolean(
        string="Is extension",
        tracking=True)
    is_extension_stage = fields.Boolean(
        string="Is extension stage",
        compute="_compute_extension_stage")
    recurring_rule_boundary = fields.Selection(
        string="Duration",
        related="template_id.recurring_rule_boundary")
    document_ids = fields.Many2many(
        'ir.attachment',
        string="SUBA SU ARCHIVO",
        help='Please attach Documents',
        copy=False,
        tracking=True)
    low_date = fields.Date(
        string="Low date")
    res_partner_low_mto_id = fields.Many2one(
        'res.partner',
        string="Low mto")
    is_suspension_stage = fields.Boolean(
        string="Is suspension stage")
    check_signature = fields.Boolean(
        string="Check signature")
    pdf_file_welcome = fields.Binary(
        string="PDF file welcome",
        compute="action_get_attachment")
    signature_url_text = fields.Text(
        string="Signature URL")
    stage_code = fields.Char(
        string="Code",
        related="stage_id.stage_code")
    

    def action_welcome_email_send(self):
        self.contract_send = True
        self.ensure_one()
        template = self.env.ref('sat_companies_sale_suscription.template_email_welcome')
        lang = self.env.context.get('lang')
        template_id = template.id
        if template.lang:
            lang = template._render_lang(self.ids)[self.id]
        ctx = {
            'default_model': 'sale.subscription',
            'default_res_id': self.ids[0],
            'default_use_template': bool(template_id),
            'default_template_id': template_id,
            'default_composition_mode': 'comment',
            'mark_so_as_sent': True,
            'custom_layout': "mail.mail_notification_paynow",
            'proforma': self.env.context.get('proforma', False),
            'force_email': True,
            'model_description': self.with_context(lang=lang).type_name,
        }
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(False, 'form')],
            'view_id': False,
            'target': 'new',
            'context': ctx,
        }
    
    def _compute_file_welcome_email(self):
        pdf = self.env.ref('sat_companies_sale_suscription.template_email_welcome').render_qweb_pdf(self.ids)
        b64_pdf = base64.b64encode(pdf[0])


    @api.depends('check_signature')
    def action_get_attachment(self):
        for record in self:
            if record.check_signature == True:
                pdf = self.env.ref('sat_companies_sale_suscription.template_email_welcome')._render_qweb_pdf(self.ids)
                print(pdf)
                b64_pdf = base64.b64encode(pdf[0])
                record.pdf_file_welcome = b64_pdf
                if record.order_line:
                    for line in record.order_line:
                        line.subscription_id.pdf_file_sale_contract = record.pdf_file_welcome
            else:
                record.pdf_file_welcome = False
    

    def button_rejected_stage(self):
        rs = self.env['sale.subscription.stage'].search([('stage_code', '=', '1')], limit=1)
        self.write({'stage_id': rs.id})


    @api.onchange('product_id')
    def onchange_product_gadget_id(self):
        if self.product_id:
            self.low_date = self.product_id.low_date
            self.res_partner_low_mto_id = self.product_id.res_partner_low_mto_id.id


    @api.depends('stage_id')
    def _compute_extension_stage(self):
        for record in self:
            if record.stage_id.stage_code == '2':
                record.is_extension_stage = True
            else:
                record.is_extension_stage = False
    

    @api.onchange('stage_id')
    def _compute_suspension_stage(self):
        for record in self:
            if record.stage_id.stage_code == '01':
                record.is_suspension_stage = True
            else:
                record.is_suspension_stage = False


    @api.onchange('product_id')
    def _template_gadget(self):
        for record in self:
            record.template_id = record.product_id.subscription_template_id


    @api.onchange('partner_id')
    def onchange_partner_id(self):
        res = super(SaleSuscriptionInherit, self).onchange_partner_id()
        for record in self:
            if record.partner_id.payment_term_maintenance_id:
                record.payment_term_id = record.partner_id.payment_term_maintenance_id
                """
                vals = {
                    'payment_term_id': record.partner_id.payment_term_maintenance_id.id
                }
                record.sudo().write(vals)
                """
        return res

    def start_subscription(self):
        res = super(SaleSuscriptionInherit, self).start_subscription()
        for record in self:
            project_fsm = self.env.ref('industry_fsm.fsm_project', raise_if_not_found=False)

            new_task = self.env['project.task'].sudo().create({
                'name': record.name,
                'partner_id': record.partner_id.id,
                'ot_type_id': record.sale_type_id.id,
                'gadgest_contract_type_id': record.gadgest_contract_type_id.id,
                'project_id': project_fsm.id,
                'user_id': record.task_user_id.id,
                'product_id': record.product_id.id,
                'planned_date_begin': record.date_begin, 
                'planned_date_end': record.date_end,
                'is_fsm': True

            })
            """
            if record.recurring_invoice_line_ids:
                for line in record.recurring_invoice_line_ids.order_line:
                    line.task_id = new_task.id
            """
        return res


    @api.onchange('product_id')
    def onchange_check_product(self):
        for record in self:
            if record.product_id.employee_notice_id.user_id:
                record.task_user_id = record.product_id.employee_notice_id.user_id
            sale_type = record.product_id.subscription_template_id.sale_type_id
            gadgets_contract = record.product_id.subscription_template_id.gadgets_contract_type_id
            record.sale_type_id = sale_type
            record.gadgest_contract_type_id = gadgets_contract


    @api.depends('sale_type_id')
    def _compute_check_contract_type(self):
        for record in self:
            record.type_contract = False
            if record.sale_type_id.code == '01':
                record.check_contract_type = True
            else:
                record.check_contract_type = False


    @api.constrains('partner_id')
    def _validate_is_potential_client(self):
        for record in self:
            if record.is_potential_client:
                raise ValidationError(_(
                    'Validate potential client in partner'))


    @api.onchange('team_id')
    def _onchange_team(self):
        for record in self:
            print('team')

    """
    @api.model
    def _cron_recurring_create_invoice(self):
        self.active_cron_invoice = True
        res = super(SaleSuscriptionInherit, self)._cron_recurring_create_invoice()
        return res
    """

    """
    def _active_cron_invoice(self,active_cron):
        active_cron = True
        return active_cron
    """


    def _recurring_create_invoice(self):
        res = super(SaleSuscriptionInherit, self)._recurring_create_invoice()
        for record in self:
            month_exclude = False
            #active_cron = record._active_cron_invoice(active_cron)
            if record.template_id.exclude_months == True:
                #if active_cron == True:
                #    date_today = datetime.now().month
                #else:
                date_today = record.recurring_next_date.month
    
                if date_today == 1 and record.template_id.jan == True:
                    month_exclude = True
                elif date_today == 2 and record.template_id.feb == True:
                    month_exclude = True
                elif date_today == 3 and record.template_id.mar == True:
                    month_exclude = True
                elif date_today == 4 and record.template_id.apr == True:
                    month_exclude = True
                elif date_today == 5 and record.template_id.may == True:
                    month_exclude = True
                elif date_today == 6 and record.template_id.jun == True:
                    month_exclude = True
                elif date_today == 7 and record.template_id.jul == True:
                    month_exclude = True
                elif date_today == 8 and record.template_id.aug == True:
                    month_exclude = True
                elif date_today == 9 and record.template_id.sep == True:
                    month_exclude = True
                elif date_today == 10 and record.template_id.oct == True:
                    month_exclude = True
                elif date_today == 11 and record.template_id.nov == True:
                    month_exclude = True
                elif date_today == 12 and record.template_id.dec == True:
                    month_exclude = True
                
                if month_exclude == True:
                    print('test')
                    #res.amount_untaxed = 0.0
                    #res.amount_untaxed_signed = 0.0
                    res.amount_by_group = False
                    #res.amount_total = 0.0
                    total = 0
                    if res.invoice_line_ids:
                        for line in res.invoice_line_ids:
                            total = line.price_subtotal
                        
                        free_month_product =self.env.ref(
                        'sat_companies_sale_suscription.free_month_product_service'
                        )
                        line_last_product = res.invoice_line_ids[-1]
                        vals = {
                                'product_id': record.product_id.id,
                                'task_user_id': record.task_user_id.id,
                                'sale_type_id': record.sale_type_id.id,
                                'gadgets_contract_type_id': record.gadgest_contract_type_id.id,
                                'invoice_line_ids': [(0, 0, {
                                    'name': 'Descuento total por mes',
                                    'product_id': free_month_product.id,
                                    'tax_ids': line_last_product.tax_ids.ids,
                                    'price_unit': -total,
                                    'quantity': 1,
                                    })]
                                    }
                        res.write(vals)
                    else:
                        vals = {
                            'product_id': record.product_id.id,
                            'task_user_id': record.task_user_id.id,
                            'sale_type_id': record.sale_type_id.id,
                            'gadgets_contract_type_id': record.gadgest_contract_type_id.id,
                            }
                        res.write(vals)
                else:
                    vals = {
                            'product_id': record.product_id.id,
                            'task_user_id': record.task_user_id.id,
                            'sale_type_id': record.sale_type_id.id,
                            'gadgets_contract_type_id': record.gadgest_contract_type_id.id,
                            }
                    res.write(vals)
                        #line.amount_currency = 0.0
                        #line.price_unit = 0.0
                        #line.discount = 100
                        #line.recompute_tax_line = True
                        #line._onchange_mark_recompute_taxes()
                        #line.tax_ids = False
                        #res._compute_base_line_taxes(line)

                    #res._compute_invoice_taxes_by_group()
                    #res._onchange_invoice_line_ids()
                        #break
                    #res._recompute_dynamic_lines(recompute_all_taxes=True, recompute_tax_base_amount=True)
                    #res._recompute_tax_lines(recompute_tax_base_amount=False)
            else:
                vals = {
                        'product_id': record.product_id.id,
                        'task_user_id': record.task_user_id.id,
                        'sale_type_id': record.sale_type_id.id,
                        'gadgets_contract_type_id': record.gadgest_contract_type_id.id,
                        }
                res.write(vals)
            active_cron = False

        return res
