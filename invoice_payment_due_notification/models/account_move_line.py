# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import date, timedelta
import logging
_logger = logging.getLogger(__name__)



class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'


    x_send_notification = fields.Boolean('Send notification', default=False, compute='_compute_x_send_notification', store=True, copy=False)
    x_last_notification = fields.Date('Last notification', help='Last notification sent date', copy=False)


    #Método para calcular si se debe enviar la notificación de ese apunte o no, en función de las condiciones requeridas (2 días después del vencimiento y sólo 1 por semana).
    @api.depends('parent_state', 'move_id.payment_state', 'date_maturity', 'x_last_notification')
    def _compute_x_send_notification(self):
        today = fields.Date.today()
        for record in self:
            last_day = (today - record.x_last_notification).days if record.x_last_notification else 7
            if record.date_maturity:
                record.x_send_notification = (record.journal_id.type in ['sale', 'purchase']) and (record.parent_state == 'posted') \
                and (record.move_id.payment_state in ['not_paid', 'partial']) and (record.date_maturity <= today - timedelta(days=2) and (last_day >= 7))
            else:
                record.x_send_notification = False

    #Envía notificaciones a los usuarios especificados en los Ajustes de Contabilidad.
    def _send_invoice_payment_due_notifications(self):
        company = self.company_id or self.env.company
        if not company.x_invoice_due_notification:
            return
        user_ids = company.x_invoice_due_notification_user_ids
        today = fields.Date.today()
        #payment_due_ids = self.search([('parent_state', '=', 'posted'), ('move_id.payment_state', 'in', ['not_paid', 'partial']), ('date_maturity', '<=', today - timedelta(days=2))])
        payment_due_ids = self.search([('x_send_notification', '=', True)])
        #_logger.info('\nsend_notification_to_users (before FOR) prueba:%s - factura:%s - estado:%s - user_ids:%s - today:%s - payment:%s\n', prueba, self.move_id.name, self.parent_state, user_ids, today, payment_due_ids)
        for record in payment_due_ids:
            due_days = today - record.date_maturity if record.date_maturity else -1
            _logger.info('\nsend_notification_to_users due_days:%s - factura:%s - estado:%s - user_ids:%s - vencimiento:%s - today:%s - payment:%s\n', due_days, record.move_id.name, record.parent_state, user_ids, record.date_maturity, today, record.name)
            for user in user_ids:
                subject = _('Invoice payment due notification')
                message = _('Invoice ') + record.move_id.name + _(' has a payment due on ') + record.date_maturity.strftime('%d/%m/%Y')
                res = record._send_notification('account.move', record.move_id.id, user, subject, message)
                if res:
                    record.x_last_notification = today


    #Método para enviar una notificación pasando como parámetro el modelo, el id del registro, el usuario y el asunto y el cuerpo de la notificación.
    def _send_notification(self, model, res_id, user, subject, body):
        #_logger.info('\n_send_notification - model:%s - res_id:%s - user:%s - subject:%s\n', model, res_id, user, subject)
        type = 'email' if user.notification_type == 'email' else 'notification'
        message=self.env['mail.message'].create({
            'message_type': type, #'notification',
            #'subtype_id': self.env.ref("mail.mt_comment").id, # subject type
            'subject': subject,
            'body': body,
            'partner_ids': [(4, user.partner_id.id)],   # partner to whom you send notification
            'model': model,
            'res_id': res_id,
            'author_id': 2, #Odoobot
            'is_internal': True,
        })
        notif_values = {
            'mail_message_id': message.id,
            'res_partner_id': user.partner_id.id,
            'notification_type': user.notification_type, #'inbox',
            'notification_status': 'sent',
        }
        _logger.info('\n_send_notification - message:%s - notif_values:%s\n', message, notif_values)
        res = self.env['mail.notification'].create(notif_values)
        return res
