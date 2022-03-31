# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class CrmLeadType(models.Model):
    _name = 'crm.lead.type'
    _inherit = 'mail.thread'
    _description = 'Oportunity type'

    name = fields.Char(String="Name", tracking=True)
    active = fields.Boolean(string="Active", default=True)
    