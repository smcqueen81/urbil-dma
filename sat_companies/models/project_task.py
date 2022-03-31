from odoo import models, fields, api

class ProjectTask(models.Model):
    _inherit = 'project.task'

    minute_point_ids = fields.Many2many(
        'maintenance.minute.point',
        string="Minute point")
    checklist_line_ids = fields.One2many(
        'project.task.ot.checklist.line',
        'task_id',
        string="checklist lines")
    checklist_ids = fields.Many2many(
        'project.task.ot.checklist',
        string="Checklist",
        tracking=True)
    inspection_id = fields.Many2one(
        'project.task.inspection',
        string="Inspection",
        tracking=True)
