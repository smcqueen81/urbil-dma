# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class SaleOrderType(models.Model):
    _name = 'sale.order.type'
    _inherit = 'mail.thread'
    _description = 'Sale order type'

    name = fields.Char(
        string="Name",
        tracking=True)
    code = fields.Char(
        string="Code",
        tracking=True)
    active  = fields.Boolean(
        string="Active",
        tracking=True,
        default=True)
    is_create_task = fields.Boolean(
        string="Create task",
        tracking=True)
    project_stage_ids = fields.Many2many(
        'project.task.type',
        string="Stages",
        tracking=True)
    project_task_ids = fields.Many2many(
        'project.task',
        string="Tasks",
        tracking=True)
    is_maintenance = fields.Boolean(
        string="Is maintenance")
    is_line = fields.Boolean(
        string="Is line")
    is_other = fields.Boolean(
        string="Other")
    is_mounting = fields.Boolean(
        string="Is mounting")


    @api.onchange('name')
    def _upper_name(self):        
        self.name = self.name.upper() if self.name else False


    @api.depends('name')
    def _compute_check_is_maintenance(self):
        for record in self:
            record.is_maintenance = True if record.name == 'MANTENIMIENTO' else False
            record.is_line = True if record.name == 'LINEA' else False
