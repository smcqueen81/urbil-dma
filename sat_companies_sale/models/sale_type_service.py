# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class SaleTypeService(models.Model):
    _name = 'sale.type.service'

    name = fields.Char(string="Name")
    item = fields.Integer()
    code = fields.Char(string="Code")
    active = fields.Boolean(string="Active")
    order_id = fields.Many2one('sale.order', string="Sale Order")