# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    code = fields.Char(
        string="Code",
        tracking=True,
        readonly=True,
        required=True,
        copy=False,
        default='New')
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
    comunities_ids = fields.Many2many(
        'res.company',
        'partner_comunity_company_rel'
    )
    admin_id = fields.Many2one(
        'res.partner',
        domain=[('is_admin', '=', True)]
    )


    # Ejecutar Secuencia 
    @api.model
    def create(self, vals):
        if vals.get('code', 'New') == 'New':
            vals['code'] = self.env['ir.sequence'].next_by_code('partner') or 'New'
        result = super(ResPartner, self).create(vals)
        return result


    @api.constrains('percentaje_mto', 'percentaje_rep')
    def _validate_percentage(self):
        for record in self:
            if record.percentaje_rep > 100 or record.percentaje_mto > 100:
                raise ValidationError(_(
                    'The percentage cannot be greater than 100'))


    @api.onchange('company_type')
    def _validate_company_type(self):
        for record in self:
            if record.company_type == 'company':
                record.is_potential_client = True
            else:
                record.is_potential_client = False


    @api.constrains('name','is_potential_client')
    def _validate_is_potential_client_identification(self):
        for record in self:
            if record.company_type == 'company':
                if record.is_potential_client != True:
                    if not record.bank_ids:
                        raise ValidationError(_('The bank account field must be filled out'))


    @api.constrains('name','is_potential_client')
    def _validate_is_potential_client_vat(self):
        for record in self:
            if record.company_type == 'company':
                if record.is_potential_client != True:
                    if not record.vat:
                        raise ValidationError(_('The identification number field must be filled out'))


    @api.constrains('name','is_potential_client')
    def _validate_is_potential_client_contact_address(self):
        for record in self:
            if record.company_type == 'company':
                if record.is_potential_client != True:
                    if not record.contact_address:
                        raise ValidationError(_('The contact address field must be filled out'))


    @api.constrains('name','is_potential_client')
    def _validate_is_potential_client_street(self):
        for record in self:
            if record.company_type == 'company':
                if record.is_potential_client != True:
                    if not record.street:
                        raise ValidationError(_('The street field must be filled out'))


    @api.constrains('name','is_potential_client')
    def _validate_is_potential_client_city(self):
        for record in self:
            if record.company_type == 'company':
                if record.is_potential_client != True:
                    if not record.city:
                        raise ValidationError(_('The city field must be filled out'))


    @api.constrains('name','is_potential_client')
    def _validate_is_potential_client_country(self):
        for record in self:
            if record.company_type == 'company':
                if record.is_potential_client != True:
                    if not record.country_id:
                        raise ValidationError(_('The country field must be filled out'))


    @api.constrains('name','is_potential_client')
    def _validate_is_potential_client_state(self):
        for record in self:
            if record.company_type == 'company':
                if record.is_potential_client != True:
                    if not record.state_id:
                        raise ValidationError(_('The state field must be filled out'))


    @api.constrains('name','is_potential_client')
    def _validate_is_potential_client_cp(self):
        for record in self:
            if record.company_type == 'company':
                if record.is_potential_client != True:
                    if not record.zip:
                        raise ValidationError(_('The postal code field must be filled out'))
    
