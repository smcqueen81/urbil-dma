# Copyright 2021 Process Control
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    date_join = fields.Date(string="Join Date", groups='hr.group_hr_user')
    date_termination = fields.Date(string="Termination Date", groups='hr.group_hr_user')
    date_on_work = fields.Date(string="Fecha de Alta", groups='hr.group_hr_user')
    ss_number = fields.Char(string="SS Number", groups='hr.group_hr_user')
    imei_number = fields.Char(string="Imei Number", groups='hr.group_hr_user')
    vehicle_number = fields.Char(string="Vehicle Number", groups='hr.group_hr_user')
    pda_id = fields.Char(string="PDA Id", groups='hr.group_hr_user')
    pda_code = fields.Char(string="PDA Code", groups='hr.group_hr_user')
    alarm_code = fields.Char(string="Alarm Code", groups='hr.group_hr_user')
