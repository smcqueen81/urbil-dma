# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class SaleOrderGadgets(models.Model):
    _name = 'sale.gadgets'
    _inherit = 'mail.thread'
    _description = 'Gadgets'
    _rec_name = 'code'

    code = fields.Char(
        string="Code",
        tracking=True,
        readonly=True,
        required=True,
        copy=False,
        default='New')
    partner_id = fields.Many2one(
        'res.partner',
        string="Client",
        tracking=True)
    domicile = fields.Char(string="Domicile", tracking=True)
    ref_type = fields.Char(string="Type", tracking=True)
    inspection_date = fields.Date(
        string="Last inspection date",
        tracking=True)
    next_inspection_date = fields.Date(
        string="next inspection date",
        tracking=True)
    pending_date_corrected = fields.Date(
        string="Pending date to be corrected",
        tracking=True)
    correction_date = fields.Date(
        string="Date of correction",
        tracking=True)
    years = fields.Selection([
        ('two','2 years'),
        ('four','4 years'),
        ('six','6 years')],string="Years", tracking=True)
    use = fields.Char(string="Use")
    state_gadget = fields.Char(string="State")
    type_contract = fields.Selection([
        ('normal','Normal'),
        ('all_risk','All risk')],string="Type of contract",tracking=True)
    type_assistance = fields.Char(
        string="Type assistance",
        tracking=True)
    is_priority = fields.Boolean(
        string="Is priority",
        tracking=True)
    is_full_service = fields.Boolean(
        string="Is 24H",
        tracking=True)
    keys = fields.Char(
        string="Keys",
        tracking=True)
    edifice = fields.Char(
        string="Edifice",
        tracking=True)
    high_date_call_center = fields.Date(
        string="High date call center",
        tracking=True)
    population_id = fields.Many2one(
        'res.partner.population',
        string="Population",
        tracking=True)
    user_id = fields.Many2one(
        'res.users',
        string="Admin",
        tracking=True)
    location = fields.Char(
        string="Location",
        tracking=True)
    type_gadget = fields.Char(
        string="Type",
        tracking=True)
    high_date = fields.Date(
        string="High date",
        tracking=True)
    end_guarantee = fields.Char(
        string="End guarantee",
        tracking=True)
    end_date_contract = fields.Date(
        string="End date contract",
        tracking=True)
    start_date_contract = fields.Date(
        string="Start contract date",
        tracking=True)
    high_mto_company = fields.Char(
        string="High Mto company",
        tracking=True)
    contract_number = fields.Char(
        string="N° contract",
        tracking=True)
    invoice_start_date = fields.Date(
        string="Invoice start date",
        tracking=True)
    years_extended = fields.Integer(
        string="Years of extended",
        tracking=True)
    extended_date = fields.Date(
        string="Extended date",
        tracking=True)
    start_up_date = fields.Date(
        string="Start up date",
        tracking=True)
    low_date = fields.Date(
        string="Low date",
        tracking=True)
    low_mto_company = fields.Date(
        string="Low Mto company",
        tracking=True)
    billing_period  = fields.Char(
        string="Billing period",
        tracking=True)
    type_increase = fields.Char(
        string="Type of increase",
        tracking=True)

    # Ejecutar Secuencia 
    @api.model
    def create(self, vals):
        if vals.get('code', 'New') == 'New':
            vals['code'] = self.env['ir.sequence'].next_by_code('gadgets') or 'New'
        result = super(SaleOrderGadgets, self).create(vals)
        return result
