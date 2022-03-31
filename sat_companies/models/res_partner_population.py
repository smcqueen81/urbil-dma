# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class ResPartnerPopulation(models.Model):
    _name = 'res.partner.population'
    _inherit = 'mail.thread'
    _description = 'Population'

    name = fields.Char(String="Partner's type", tracking=True)
    code = fields.Char(string="Code", tracking=True)
