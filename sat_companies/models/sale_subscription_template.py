# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class SaleSubscriptionTemplate(models.Model):
    _inherit = 'sale.subscription.template'

    is_maintenance = fields.Boolean(
        string="Is a maintenance",
        tracking=True)
    type_contract = fields.Selection([
        ('normal','Normal'),
        ('all_risk','All risk')],string="Type of contract",tracking=True)
