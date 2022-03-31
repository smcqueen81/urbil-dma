# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    delegation_id = fields.Many2one(
        'res.partner.delegation',
        string="Delegation",
        tracking=True)
    delegation_code = fields.Char(
        string="Code",
        tracking=True)
    c_accountant = fields.Char(
        string="C.Accountant",
        tracking=True)
    alarm_code = fields.Char(
        string="Alarm code",
        tracking=True)
    shirt_size = fields.Char(
        string="Shirt size",
        tracking=True)
    shoe_size = fields.Char(
        string="Shoe size",
        tracking=True)
    jersey_size = fields.Char(
        string="Jersey size",
        tracking=True)
    parka_size = fields.Char(
        string="Parka size",
        tracking=True)
    jacket_size = fields.Char(
        string="Jacket size",
        tracking=True)
    pants_size = fields.Char(
        string="Pants size",
        tracking=True)
    polo_size = fields.Char(
        string="Polo size",
        tracking=True)
    raincoat_size = fields.Char(
        string="Raincoat size",
        tracking=True)
    pda = fields.Boolean(
        string="PDA",
        tracking=True)
    online_service = fields.Boolean(
        string="Online services",
        tracking=True)
    supervisor = fields.Boolean(
        string="Supervisor",
        tracking=True)
    warehouse = fields.Char(
        string="Warehouse",
        tracking=True)
    workwear = fields.Boolean(
        string="Workwear",
        tracking=True)
    password = fields.Char(
        string="Password",
        tracking=True)
    imei = fields.Char(string="IMEI")
    type_driving_license = fields.Char(
        string="Type driving license",
        tracking=True)
    employee_type = fields.Many2one(
        'hr.employee.type',
        string="Employee type")
    is_maintainer = fields.Boolean(
        string="Is maintainer",
        tracking=True)
    category_id = fields.Many2one(
        'hr.employee.categories',
        string="Employee category",
        tracking=True)
    warehouse_id = fields.Many2one(
        'stock.warehouse',
        string="Warehouse",
        tracking=True)
