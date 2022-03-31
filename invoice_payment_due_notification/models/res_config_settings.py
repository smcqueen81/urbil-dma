# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
import logging
_logger = logging.getLogger(__name__)

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    
    x_invoice_due_notification = fields.Boolean(string="Invoices due notification")
    x_invoice_due_notification_user_ids = fields.Many2many('res.users', 'res_config_settings_res_users_rel', string="Users")

    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res.update(
            x_invoice_due_notification = self.env.user.company_id.x_invoice_due_notification,
            x_invoice_due_notification_user_ids = self.env.user.company_id.x_invoice_due_notification_user_ids
        )
        return res

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        company_id = self.env.user.company_id
        company_id.x_invoice_due_notification = self.x_invoice_due_notification
        company_id.x_invoice_due_notification_user_ids = self.x_invoice_due_notification_user_ids
