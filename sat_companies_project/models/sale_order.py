# -*- coding: utf-8 -*-
from typing import DefaultDict
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import logging

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    sale_type_id = fields.Many2one(
        'sale.order.type',
        string="Sale type",
        tracking=True)
    is_potential_client = fields.Boolean(
        string="Is a potential client",
        tracking=True,
        related="partner_id.is_potential_client")
    udn_id = fields.Many2one(
        'project.task.categ.udn',
        string="Udn")
    is_forecast_made = fields.Boolean(
        string="Is forecast made")
    is_maintenance = fields.Boolean(
        string="Is maintenance",
        related="sale_type_id.is_maintenance")
    is_mounting = fields.Boolean(
        string="Is mounting")
    is_normative = fields.Boolean(
        string="Normative",
        related="udn_id.is_normative")
    normative_date = fields.Date(
        string="Normative date")
    

    @api.onchange(
        'sale_order_type',
        'udn_id')
    def onchange_so_type(self):
        if self.sale_type_id:
            self.is_mounting = self.sale_type_id.is_mounting


    def get_task_sale_type(self):
        for record in self:
            if record.sale_order_template_id:
                sale_order_template = str(record.sale_order_template_id.name+' - ')
            else:
                sale_order_template = ''

            if record.sale_type_id:
                order_type_form = record.env.ref('sat_companies_project.wizard_sale_order_type_form',raise_if_not_found=False)
                ctx = dict(
                    default_name = str(sale_order_template + record.name+' - '+ record.partner_id.name),
                    default_model='wizard.sale.order.type',
                    default_sale_order_id=record.id,
                    default_sale_type_id=record.sale_type_id.id,
                    default_project_line_ids= record.order_line.ids
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
                record.action_confirm()

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        if self.is_potential_client:
            raise ValidationError(_("Verify the type of client if it is potential"))
            return res

    @api.onchange(
        'partner_id',
        'sale_type_id',
        'product_id')
    def onchange_partner(self):
        for record in self:
            if record.sale_type_id.is_maintenance:
                record.payment_term_id = record.partner_id.payment_term_maintenance_id
            elif record.sale_type_id.is_line:
                record.payment_term_id = record.partner_id.payment_term_tel_id
            else:
                record.payment_term_id = record.partner_id.property_payment_term_id
