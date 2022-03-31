# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class SaleOrderContractLine(models.Model):
    _name = 'sale.order.contract.line'
    _inherit = 'mail.thread'
    _description = 'Contract lines'

    name = fields.Char(string="Name", tracking=True)
    sale_id = fields.Many2one(
        'sale.order',
        string="Sale order",
        tracking=True)
    contact_id = fields.Many2one(
        'sale.order.contract',
        string="Item",
        tracking=True)
    description = fields.Html(
        string="Description",
        related="contact_id.description")
