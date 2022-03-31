# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class ResPartnerType(models.Model):
    _name = 'res.partner.type'
    _inherit = 'mail.thread'
    _description = 'Partner type'

    name = fields.Char(String="Partner's type", tracking=True)
    code = fields.Char(string="Code", tracking=True)
