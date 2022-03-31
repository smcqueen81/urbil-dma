# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class MaintenanceMinutePoint(models.Model):
    _name = 'maintenance.minute.point'
    _inherit = 'mail.thread'
    _description = 'Minute point'

    name = fields.Char(
        String="Zone's name",
        tracking=True)
    code = fields.Char(
        string='Code',
        tracking=True,
        readonly=True,
        required=True,
        copy=False,
        default='New')
    description = fields.Text(
        string="Description",
        tracking=True)
    type_deffect_id = fields.Many2one(
        'maintenance.type.deffect',
        string="Type of deffect",
        tracking=True)

    # Sequence
    @api.model
    def create(self, vals):
        if vals.get('code', 'New') == 'New':
            vals['code'] = self.env['ir.sequence'].next_by_code('minute.point') or 'New'
        result = super(MaintenanceMinutePoint, self).create(vals)
        return result