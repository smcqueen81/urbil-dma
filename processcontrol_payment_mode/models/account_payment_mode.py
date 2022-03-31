import time

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class AccountPaymentOrder(models.Model):
    _inherit = 'account.payment.mode'

    offsetting_account = fields.Selection(
        selection=[
            ("bank_account", "Bank Account"),
            ("transfer_account", "Transfer Account"),
        ],
        default="bank_account",
    )
    transfer_account_id = fields.Many2one(
        comodel_name="account.account",
        domain=[("reconcile", "=", True)],
        help="Pay off lines in 'file uploaded' payment orders with a move on "
             "this account. You can only select accounts "
             "that are marked for reconciliation",
        check_company=True,
    )
    transfer_journal_id = fields.Many2one(
        comodel_name="account.journal",
        help="Journal to write payment entries when confirming "
             "payment/debit orders of this mode",
        check_company=True,
    )

    @api.constrains("offsetting_account", "transfer_account_id", "transfer_journal_id")
    def transfer_move_constrains2(self):
        for mode in self:
            if mode.generate_move:
                if not mode.offsetting_account:
                    raise ValidationError(
                        _(
                            "On the payment mode '%s', you must select an "
                            "option for the 'Offsetting Account' parameter"
                        )
                        % mode.name
                    )
                elif mode.offsetting_account == "transfer_account":
                    if not mode.transfer_account_id:
                        raise ValidationError(
                            _(
                                "On the payment mode '%s', you must "
                                "select a value for the 'Transfer Account'."
                            )
                            % mode.name
                        )
                    if not mode.transfer_journal_id:
                        raise ValidationError(
                            _(
                                "On the payment mode '%s', you must "
                                "select a value for the 'Transfer Journal'."
                            )
                            % mode.name
                        )

    @api.onchange("generate_move")
    def generate_move_change(self):
        super(AccountPaymentOrder, self).generate_move_change()
        if self.generate_move:
            self.offsetting_account = "bank_account"
        else:
            self.offsetting_account = False
            self.transfer_account_id = False
            self.transfer_journal_id = False

    @api.onchange("offsetting_account")
    def offsetting_account_change(self):
        if self.offsetting_account == "bank_account":
            self.transfer_account_id = False
            self.transfer_journal_id = False
