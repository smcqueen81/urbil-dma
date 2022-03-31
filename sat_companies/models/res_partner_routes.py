# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class ResPartnerRoutes(models.Model):
    _name = 'res.partner.routes'
    _inherit = 'mail.thread'
    _description = 'Routes'

    name = fields.Char(
        String="Zone's name",
        tracking=True)
    code = fields.Char(
        string="Code", 
        tracking=True,
        readonly=True,
        required=True,
        copy=False,
        default='New')
    country_id = fields.Many2one(
        'res.country',
        string="Country",
        tracking=True)
    route_type = fields.Selection([
        ('normal','Normal'),
        ('guard','Guard')],string="Route type",tracking=True)
    zone_ids = fields.Many2many(
        'res.partner.zones',
        string="Zones",
        tracking=True)
    user_operator_id = fields.Many2one(
        'hr.employee',
        string="Operator notice")
    user_operator_greasing_id = fields.Many2one(
        'hr.employee',
        string="Operator greasing")
    employee_id = fields.Many2one(
        'hr.employee',
        string="Responsable")


    # Ejecutar Secuencia 
    @api.model
    def create(self, vals):
        if vals.get('code', 'New') == 'New':
            vals['code'] = self.env['ir.sequence'].next_by_code('route') or 'New'
        result = super(ResPartnerRoutes, self).create(vals)
        return result
