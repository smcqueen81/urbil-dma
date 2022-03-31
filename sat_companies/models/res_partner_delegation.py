# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class ResPartnerDelegation(models.Model):
    _name = 'res.partner.delegation'
    _inherit = 'mail.thread'
    _description = 'Zones'

    name = fields.Char(String="Zone's name", tracking=True)
    code = fields.Char(string="Postal Code", tracking=True)
    country_id = fields.Many2one(
        'res.country',
        string="Country",
        tracking=True)
