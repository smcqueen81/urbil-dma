# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class MaintenanceTypeDeffect(models.Model):
    _name = 'maintenance.type.deffect'
    _inherit = 'mail.thread'
    _description = 'Type deffect'

    name = fields.Char(
        String="Zone's name",
        tracking=True)
    description = fields.Text(
        string="Description",
        tracking=True)