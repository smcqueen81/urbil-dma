# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class StockLandingDoors(models.Model):
    _name = 'stock.landing.doors'
    _inherit = 'mail.thread'
    _description = 'Landing doors'

    name = fields.Char(
        string="Name",
        tracking=True)
    active = fields.Boolean(
        string="Active",
        tracking=True,
        default=True)

    @api.onchange('name')
    def _upper_name(self):        
        self.name = self.name.upper() if self.name else False
