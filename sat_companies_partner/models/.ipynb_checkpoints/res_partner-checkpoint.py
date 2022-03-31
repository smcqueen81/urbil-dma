# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import logging
import re

class ResPartner(models.Model):
    _inherit = 'res.partner'

    code = fields.Char(
        string="Code",
        tracking=True,
        copy=False)
    high_date = fields.Date(
        string="High date",
        tracking=True)
    low_date = fields.Date(
        string="Low date",
        tracking=True)
    partner_type_id = fields.Many2one(
        'res.partner.type',
        string="Partner type",
        tracking=True)
    resource_calendar_id = fields.Many2one(
        'resource.calendar',
        string="Resource calendar",
        tracking=True)
    delegation_id = fields.Many2one(
        'res.partner.delegation',
        string="Delegation",
        tracking=True)
    observations = fields.Text(
        string="Observaciones",
        tracking=True)
    percentaje_mto = fields.Float(
        string="Ges.Mto",
        tracking=True)
    percentaje_rep = fields.Float(
        string="Ges.Rep",
        tracking=True)
    percentaje_ges_mto = fields.Float(
        string="%",
        related="percentaje_mto",
        tracking=True)
    percentaje_ges_rep = fields.Float(
        string="%",
        related="percentaje_rep",
        tracking=True)
    user_partner_id = fields.Many2one(
        'res.users',
        string="User",
        tracking=True)
    password_user = fields.Char(
        string="Password",
        tracking=True)
    population_id = fields.Many2one(
        'res.partner.population',
        string="Population",
        tracking=True)
    contact_person = fields.Char(
        string="Contact person",
        tracking=True)
    phone1 = fields.Char(
        string="Phone 1",
        tracking=True)
    phone2 = fields.Char(
        string="Phone 2",
        tracking=True)
    phone3 = fields.Char(
        string="Phone 3",
        tracking=True)
    fax = fields.Char(
        string="Fax",
        tracking=True)
    email_address = fields.Char(
        string="Email",
        tracking=True)
    user_partner_contact_id = fields.Many2one(
        'res.users',
        string="Commercial",
        tracking=True)
    is_potential_client = fields.Boolean(
        string="Is a potential client",
        tracking=True)
    fiscal_name = fields.Char(
        string="Fiscal name",
        tracking=True)
    fiscal_name2 = fields.Char(
        string="Fiscal name 2",
        tracking=True)
    is_admin = fields.Boolean(
        string="Is Admin",
        tracking=True)
    country_state_id = fields.Many2one(
        'res.country.state',
        string="State",
        tracking=True)
    observations_oca = fields.Text(
        string="Observations",
        tracking=True)
    is_maintainer = fields.Boolean(
        string="Is maintainer",
        tracking=True)
    comunities_ids = fields.One2many(
        'res.partner.communities',
        'partner_id'
    )
    is_oca = fields.Boolean(
        string="O.C.A",
        tracking=True)
    client_code = fields.Char(
        string="Code",
        tracking=True,
        copy=False)
    gadget_ids = fields.Many2many(
        'product.template',
        compute="compute_gadgets_partner",
        string='Gadgets')
    partner_community_id = fields.One2many(
        'res.partner.communities',
        'partner_id',
        string="Community")
    delegation_name = fields.Char(
        string="Delegation name",
        related="delegation_id.name")
    gadget_client_ids = fields.Many2many(
        'product.template',
        compute="compute_gadgets_client",
        string='Gadgets')
    gadget_oca_ids = fields.Many2many(
        'product.template',
        compute="compute_gadgets_oca",
        string='Gadgets')
    gadget_maintener_ids = fields.Many2many(
        'product.template',
        compute="compute_gadgets_comunities",
        string='Gadgets')

    
    _sql_constraints = [
        (
            'client_code_uniq',
            'unique(client_code)',
            'The client code is unique!'
        )
    ]

    def compute_gadgets_partner(self):
        for record in self:
            products = self.env['product.template'].search([('partner_admin_id','=',self.id)])
            if products:
                record.gadget_ids = products.ids
            else:
                record.gadget_ids = False


    def compute_gadgets_client(self):
        for record in self:
            products = self.env['product.template'].search([('partner_id','=',self.id)])
            if products:
                record.gadget_client_ids = products.ids
            else:
                record.gadget_client_ids = False


    def compute_gadgets_oca(self):
        for record in self:
            products = self.env['product.template'].search([('partner_oca_id','=',self.id)])
            if products:
                record.gadget_oca_ids = products.ids
            else:
                record.gadget_oca_ids = False


    def compute_gadgets_comunities(self):
        for record in self:
            products = self.env['product.template'].search([('res_partner_high_mto_id','=',self.id)])
            if products:
                record.gadget_maintener_ids = products.ids
            else:
                record.gadget_maintener_ids = False


    @api.constrains('percentaje_mto', 'percentaje_rep')
    def _validate_percentage(self):
        for record in self:
            if record.percentaje_rep > 100 or record.percentaje_mto > 100:
                raise ValidationError(_(
                    'The percentage cannot be greater than 100'))


    @api.constrains('phone')
    def validate_phone(self):
        for rec in self:
            if rec.phone:
                if len(rec.phone) < 6 or re.match(r"^[a-zA-Z][ a-zA-Z]*", rec.phone):
                    raise ValidationError(_(
                        'The phone number cannot contain letters'))


    @api.constrains('mobile')
    def validate_mobile(self):
        for rec in self:
            if rec.mobile:
                if len(rec.mobile) < 10 or re.match(r"^[a-zA-Z][ a-zA-Z]*", rec.mobile):
                    raise ValidationError(_(
                        'The mobile number cannot contain letters'))


    @api.constrains('email')
    def validate_email(self):
        for rec in self:
            if rec.email:
                if not re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", rec.email):
                    raise ValidationError(_(
                    'Invalid email format!'))


    @api.onchange('name')
    def _upper_contact_name(self):        
        self.name = self.name.upper() if self.name else False
