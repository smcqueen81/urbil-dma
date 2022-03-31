# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    address = fields.Char(
        string="Address",
        related="partner_id.street",
        tracking=True)
    population_id = fields.Many2one(
        'res.partner.population',
        string="Population",
        tracking=True)
    is_potential_client = fields.Boolean(
        string="Is a potential client",
        tracking=True)
    sale_type = fields.Selection([
        ('maintenance','Maintenance'),
        ('mounting','Mounting'),
        ('repair','Repair')],string="Sale type")
    contract_line_ids = fields.One2many(
        'sale.order.contract.line',
        'sale_id',
        string="Contract lines",
        tracking=True)
    sale_type_id = fields.Many2one(
        'sale.order.type',
        string="Sale type",
        tracking=True)
    is_create_task = fields.Boolean(
        string="Create task",
        tracking=True,
        related="sale_type_id.is_create_task")


    @api.constrains('contract_line_ids')
    def _check_exist_record_in_lines(self):
        for rec in self:
            exis_record_lines = []
            for line in rec.contract_line_ids:
                if line.contact_id.id in exis_record_lines:
                    raise ValidationError(_(
                        'The item should be one per line'))
                exis_record_lines.append(line.contact_id.id)


    def get_task_sale_type(self):
        if self.sale_type_id:
            order_type_form = self.env.ref('sat_companies.wizard_sale_order_type_form',raise_if_not_found=False)
            ctx = dict(
                default_model='wizard.sale.order.type',
                default_sale_order_id=self.id,
                default_sale_type_id=self.sale_type_id.id,
            )
            return {
                'name': ('Tipo de operación'),
                'type': 'ir.actions.act_window',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'wizard.sale.order.type',
                'views': [(order_type_form.id, 'form')],
                'view_id': order_type_form.id,
                'context': ctx,
                'target': 'new',
                }
        else:
            self.action_confirm()

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        if not self.is_potential_client:
            raise ValidationError(_("Verify the type of client if it is potential"))
            return res
