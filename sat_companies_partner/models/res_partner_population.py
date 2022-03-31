# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class ResPartnerPopulation(models.Model):
    _name = 'res.partner.population'
    _inherit = 'mail.thread'
    _description = 'Population'
    _rec_name = 'code'

    name = fields.Char(
        string="Partner's type",
        tracking=True)
    code = fields.Char(
        string="Code",
        tracking=True)
    active = fields.Boolean(
        string="Active",
        tracking=True,
        default=True)

    @api.onchange('name')
    def _upper_name(self):        
        self.name = self.name.upper() if self.name else False
