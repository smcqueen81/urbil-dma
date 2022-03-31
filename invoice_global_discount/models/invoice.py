# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import UserError

class InvoiceMove(models.Model):
    _inherit = "account.move"

    global_discount = fields.Boolean("Add Global Discount", readonly=True, states={'draft': [('readonly', False)]},)
    discount_type = fields.Selection([('fixed','Fixed'),('percentage','Percentage')], 
        "Discount Type", readonly=True, states={'draft': [('readonly', False)]}, default='fixed')
    discount_amount = fields.Float("Discount Amount", readonly=True, states={'draft': [('readonly', False)]},)
    discount_percentage = fields.Float("Discount Percentage", readonly=True, states={'draft': [('readonly', False)]},)

    def _discount_unset(self):
        if self.env.user.company_id.invoice_discount_product_id:
            inv_line = self.env['account.move.line'].search([('move_id', 'in', self.ids), ('product_id', '=', self.env.user.company_id.invoice_discount_product_id.id)])
            inv_line.with_context(check_move_validity=False).unlink()

    def create_discount(self):
        InvoiceLine = self.env['account.move.line']

        product_id = self.env.user.company_id.invoice_discount_product_id
        if not product_id:
            raise UserError(_('Please set Invoice Discount product in General Settings first.'))

        # Remove Discount line first
        self._discount_unset()

        for invoice in self:
            # Account from customer
            if invoice.move_type in  ['out_invoice','out_refund','out_receipt']:
                account_id = product_id.property_account_income_id.id or product_id.categ_id.property_account_income_categ_id.id or False
                #Checking if the invoice type is sale invoice then apply sales taxes
                taxes = product_id.taxes_id.filtered(lambda t: t.company_id.id == invoice.company_id.id)
                if not account_id:
                    raise UserError(_('Please set income account on discount product.'))
                    

            # Account from supplier
            if invoice.move_type in  ['in_invoice','in_refund','in_receipt']:
                #Checking if the invoice type is purchase invoice then apply purchase taxes
                taxes = product_id.supplier_taxes_id.filtered(lambda t: t.company_id.id == invoice.company_id.id)
                account_id = product_id.property_account_expense_id.id or product_id.categ_id.property_account_expense_categ_id.id or False
                if not account_id:
                    # prop = self.env['ir.property'].get('property_account_expense_categ_id', 'product.category')
                    raise UserError(_('Please set expense account on discount product.'))

            if taxes:
                taxes_ids = taxes.ids
                if invoice.partner_id and self.fiscal_position_id:
                    taxes_ids = self.fiscal_position_id.map_tax(taxes, product_id, invoice.partner_id).ids

            amount = 0
            total = 0.0
            if invoice.discount_type == 'fixed':
                amount = invoice.discount_amount
            if invoice.discount_type == 'percentage':
                for line in invoice.invoice_line_ids:
                    total += line.price_subtotal
                amount = (total * invoice.discount_percentage)/100

            
            # Create the Invoice line
            discount_line = InvoiceLine.with_context(check_move_validity=False).create({
                'name': product_id.name,
                'price_unit': -amount,
                'account_id': account_id,
                'quantity': 1.0,
                'discount': 0.0,
                'product_uom_id': product_id.uom_id.id,
                'product_id': product_id.id,
                'move_id': invoice.id,
                'tax_ids': [(6, 0, taxes_ids)],
                'sequence': 100,
            })
            invoice.with_context(check_move_validity=False)._recompute_dynamic_lines(recompute_all_taxes=True, recompute_tax_base_amount=True)
        return True
