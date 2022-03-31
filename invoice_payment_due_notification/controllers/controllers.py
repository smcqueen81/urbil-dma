# -*- coding: utf-8 -*-
# from odoo import http


# class PcMrpCustom(http.Controller):
#     @http.route('/invoice_payment_due_notification/invoice_payment_due_notification/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/invoice_payment_due_notification/invoice_payment_due_notification/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('invoice_payment_due_notification.listing', {
#             'root': '/invoice_payment_due_notification/invoice_payment_due_notification',
#             'objects': http.request.env['invoice_payment_due_notification.invoice_payment_due_notification'].search([]),
#         })

#     @http.route('/invoice_payment_due_notification/invoice_payment_due_notification/objects/<model("invoice_payment_due_notification.invoice_payment_due_notification"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('invoice_payment_due_notification.object', {
#             'object': obj
#         })
