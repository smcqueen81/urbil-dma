# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class SaleOrderContract(models.Model):
    _name = 'sale.order.contract'
    _inherit = 'mail.thread'
    _description = 'Contract'

    name = fields.Char(string="Name", tracking=True)
    active = fields.Boolean(
        string="Active",
        tracking=True,
        default=True)
    description = fields.Html(string="Description")
