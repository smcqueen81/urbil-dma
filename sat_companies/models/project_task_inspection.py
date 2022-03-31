# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class ProjectTaskInspection(models.Model):
    _name = 'project.task.inspection'
    _inherit = 'mail.thread'
    _description = 'Inspections'

    name = fields.Char(
        String="Inspection's name",
        tracking=True)
    active = fields.Boolean(
        string="Active",
        tracking=True,
        default=True)
