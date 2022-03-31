# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class ProjectTaskOtChecklistLine(models.Model):
    _name = 'project.task.ot.checklist.line'
    _inherit = 'mail.thread'
    _description = 'OT checklist line'

    name = fields.Char(string="Name", tracking=True)
    task_id = fields.Many2one(
        'project.task',
        string="Task",
        tracking=True)
    minute_point_id = fields.Many2one(
        'maintenance.minute.point',
        string="Minute point",
        tracking=True)
    type_deffect_id = fields.Many2one(
        'maintenance.type.deffect',
        string="Type of deffect",
        tracking=True)
    is_reviewed = fields.Boolean(string="Is reviewed")
