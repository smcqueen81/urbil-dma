# -*- coding: utf-8 -*-
import string
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import datetime
from pytz import timezone

class SaleSuscriptionTemplateInherit(models.Model):
    _inherit = 'sale.subscription.template'

    sale_type_id = fields.Many2one(
        'sale.order.type',
        string="Sale type")
    type_contract = fields.Selection([
        ('normal','Normal'),
        ('risk','All risk')],string="Type of contract",tracking=True)
    gadgets_contract_type_id = fields.Many2one(
        'stock.gadgets.contract.type',
        string="Subscription type")
    exclude_months = fields.Boolean(
        'Exlude Months')
    jan = fields.Boolean(
        'January')
    feb = fields.Boolean(
        'February')
    mar = fields.Boolean(
        'March')
    apr = fields.Boolean(
        'April')
    may = fields.Boolean(
        'May')
    jun = fields.Boolean(
        'June')
    jul = fields.Boolean(
        'July')
    aug = fields.Boolean(
        'Auguts')
    sep = fields.Boolean(
        'September')
    oct = fields.Boolean(
        'October')
    nov = fields.Boolean(
        'November')
    dec = fields.Boolean(
        'December')
    days_number = fields.Integer(
        string="Days number")
    days_between_visits = fields.Integer(
        string="Days between visits")
    contract_duration = fields.Integer(
        string="Contract duration")
    contract_recurring_rule = fields.Selection([
        ('days','Days'),
        ('months','Months'),
        ('years','Years')],string="Contract recurring rule")

    """
    sale_order_template_id = fields.Many2one(
        'sale.order.template', 'Quotation Template',
        readonly=True, check_company=True,
        states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")
    """
