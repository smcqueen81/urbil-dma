# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.http import request
from odoo.exceptions import ValidationError
import base64
from io import BytesIO
import qrcode


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'


    def action_send_email(self):
        self.ensure_one()
        ir_model_data = self.env['ir.model.data']
        try:
            template_id = \
            ir_model_data.get_object_reference('sat_companies', 'sat_companies.template_account_receipt_26')[1]
        except ValueError:
            template_id = False
        try:
            compose_form_id = ir_model_data.get_object_reference('mail', 'email_compose_message_wizard_form')[1]
        except ValueError:
            compose_form_id = False
        ctx = {
           'default_model': 'account.move.line',
           'default_res_id': self.ids[0],
           'default_use_template': bool(template_id),
           'default_template_id': template_id,
           'default_composition_mode': 'comment',
        }
        return {
           'name': _('Compose Email'),
           'type': 'ir.actions.act_window',
           'view_mode': 'form',
           'res_model': 'mail.compose.message',
           'views': [(compose_form_id, 'form')],
           'view_id': compose_form_id,
           'target': 'new',
           'context': ctx,
        }
