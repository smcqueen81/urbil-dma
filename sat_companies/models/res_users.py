# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class ResUsers(models.Model):
    _inherit = 'res.users'

    route_id = fields.Many2one(
        'res.partner.routes',
        string="Normal route",
        tracking=True)
    route_type_id = fields.Many2one(
        'res.partner.routes',
        string="Guard route",
        tracking=True)
    product_ids = fields.Many2many('product.template',string="Gadgets")
