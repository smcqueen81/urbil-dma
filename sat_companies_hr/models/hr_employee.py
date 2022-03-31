# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    delegation_id = fields.Many2one(
        'res.partner.delegation',
        string="Delegation")
    delegation_code = fields.Char(
        string="Code")
    c_accountant = fields.Char(
        string="C.Accountant")
    account_id = fields.Many2one(
        'account.account',
        string="C.Accountant")
    alarm_code = fields.Char(
        string="Alarm code")
    shirt_size = fields.Char(
        string="Shirt size")
    shoe_size = fields.Char(
        string="Shoe size")
    jersey_size = fields.Char(
        string="Jersey size")
    parka_size = fields.Char(
        string="Parka size")
    jacket_size = fields.Char(
        string="Jacket size")
    pants_size = fields.Char(
        string="Pants size")
    polo_size = fields.Char(
        string="Polo size")
    raincoat_size = fields.Char(
        string="Raincoat size")
    pda = fields.Boolean(
        string="PDA")
    online_service = fields.Boolean(
        string="Online services")
    supervisor = fields.Boolean(
        string="Supervisor")
    warehouse = fields.Char(
        string="Warehouse")
    workwear = fields.Boolean(
        string="Workwear")
    password = fields.Char(
        string="Password")
    imei = fields.Char(
        string="IMEI")
    type_driving_license = fields.Char(
        string="Type driving license")
    employee_type = fields.Many2one(
        'hr.employee.type',
        string="Employee type")
    is_maintainer = fields.Boolean(
        string="Is maintainer")
    category_id = fields.Many2one(
        'hr.employee.categories',
        string="Employee category")
    warehouse_id = fields.Many2one(
        'stock.warehouse',
        string="Warehouse")
    code = fields.Char(
        string="Employee code",
        copy=False)
    delegation_name = fields.Char(
        string="Delegation name",
        related="delegation_id.name")
    employee_notes = fields.Text(
        string="Notes")


    _sql_constraints = [
        ('code_uniq', 'unique (code)','This code already exists!')
    ]

    @api.onchange(
        'shoe_size',
        'shirt_size',
        'jersey_size',
        'parka_size',
        'jacket_size',
        'pants_size',
        'polo_size',
        'raincoat_size',
        'name',
        'type_driving_license')
    def _upper_sizes(self):        
        self.shoe_size = self.shoe_size.upper() if self.shoe_size else False
        self.shirt_size = self.shirt_size.upper() if self.shirt_size else False
        self.jersey_size = self.jersey_size.upper() if self.jersey_size else False
        self.parka_size = self.parka_size.upper() if self.parka_size else False
        self.jacket_size = self.jacket_size.upper() if self.jacket_size else False
        self.pants_size = self.pants_size.upper() if self.pants_size else False
        self.polo_size = self.polo_size.upper() if self.polo_size else False
        self.raincoat_size = self.raincoat_size.upper() if self.raincoat_size else False
        self.name = self.name.upper() if self.name else False
        self.type_driving_license = self.type_driving_license.upper() if self.type_driving_license else False
