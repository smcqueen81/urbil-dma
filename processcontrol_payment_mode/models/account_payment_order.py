import time

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class AccountPaymentOrder(models.Model):
    _inherit = 'account.payment.order'

    def _prepare_move(self, bank_lines=None):
        vals = super(AccountPaymentOrder, self)._prepare_move(bank_lines)
        if self.payment_mode_id.offsetting_account == "transfer_account":
            vals['journal_id'] = self.payment_mode_id.transfer_journal_id.id
        return vals

    def _prepare_move_line_offsetting_account(self, amount_company_currency, amount_payment_currency, bank_lines):
        vals = super(AccountPaymentOrder, self)._prepare_move_line_offsetting_account(
            amount_company_currency, amount_payment_currency, bank_lines)
        if self.payment_mode_id.offsetting_account == "transfer_account":
            vals['account_id'] = self.payment_mode_id.transfer_account_id.id

        return vals
