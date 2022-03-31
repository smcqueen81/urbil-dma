from odoo import api, fields, models


class Users(models.Model):
    _inherit = 'res.users'

    #settings_id = fields.Many2one('res.config.settings', string='Settings')