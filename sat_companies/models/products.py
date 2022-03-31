# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import base64
from io import BytesIO
import qrcode

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    product_qr_code = fields.Char('QR Code')
    qr_code = fields.Binary('QR Code Image')
    qr_code_name = fields.Char(default="qr_code.png")
   

    @api.onchange('product_qr_code')
    def _generate_qr_code(self):
        if self.product_qr_code:
            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=20, border=4)
            name = self.product_qr_code + '_product.png'
            qr.add_data(self.product_qr_code)
            qr.make(fit=True)
            img = qr.make_image()
            buffer = BytesIO()
            img.save(buffer, format="PNG")
            qrcode_img = base64.b64encode(buffer.getvalue())
            self.update({'qr_code': qrcode_img, 'qr_code_name': name})

    @api.onchange('product_qr_code')
    def action_generate_qr(self):
        for record in self:
            if record.product_qr_code:
                qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=20, border=4)
                name = record.product_qr_code + '_product.png'
                qr.add_data(record.product_qr_code)
                qr.make(fit=True)
                img = qr.make_image()
                buffer = BytesIO()
                img.save(buffer, format="PNG")
                qrcode_img = base64.b64encode(buffer.getvalue())
                record.update({'qr_code': qrcode_img, 'qr_code_name': name})
            else:
                record.product_qr_code = "Prod_" + str(record.id)
                qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=20, border=4)
                name = record.product_qr_code + '_product.png'
                qr.add_data(record.product_qr_code)
                qr.make(fit=True)
                img = qr.make_image()
                buffer = BytesIO()
                img.save(buffer, format="PNG")
                qrcode_img = base64.b64encode(buffer.getvalue())
                record.update({'qr_code': qrcode_img, 'qr_code_name': name})


class ProductProductQRCode(models.Model):
    _inherit = 'product.product'

    @api.onchange('product_qr_code')
    def _generate_qr_code(self):
        if self.product_qr_code:
            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=20, border=4)
            name = self.product_qr_code + '_product.png'
            qr.add_data(self.product_qr_code)
            qr.make(fit=True)
            img = qr.make_image()
            buffer = BytesIO()
            img.save(buffer, format="PNG")
            qrcode_img = base64.b64encode(buffer.getvalue())
            self.update({'qr_code': qrcode_img, 'qr_code_name': name})

    @api.onchange('product_qr_code')
    def action_generate_qr(self):
        for record in self:
            if record.product_qr_code:
                qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=20, border=4)
                name = record.product_qr_code + '_product.png'
                qr.add_data(record.product_qr_code)
                qr.make(fit=True)
                img = qr.make_image()
                buffer = BytesIO()
                img.save(buffer, format="PNG")
                qrcode_img = base64.b64encode(buffer.getvalue())
                record.update({'qr_code': qrcode_img, 'qr_code_name': name})
            else:
                record.product_qr_code = "Prod_" + str(record.id)
                qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=20, border=4)
                name = record.product_qr_code + '_product.png'
                qr.add_data(record.product_qr_code)
                qr.make(fit=True)
                img = qr.make_image()
                buffer = BytesIO()
                img.save(buffer, format="PNG")
                qrcode_img = base64.b64encode(buffer.getvalue())
                record.update({'qr_code': qrcode_img, 'qr_code_name': name})
