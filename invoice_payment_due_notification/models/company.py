from odoo import api, fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    x_invoice_due_notification = fields.Boolean(string="Invoices due notification")
    x_invoice_due_notification_user_ids = fields.Many2many('res.users', 'res_coompany_res_users_rel', string="Users")