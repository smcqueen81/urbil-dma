from odoo import models, fields, api

class ResPartnerZones(models.Model):
    _name = 'res.partner.zones'
    _inherit = 'mail.thread'
    _description = 'Zones'

    name = fields.Char(String="Zone's name", tracking=True)
    code = fields.Char(
        string="Code", 
        tracking=True,
        readonly=True,
        required=True,
        copy=False,
        default='New')
    country_id = fields.Many2one('res.country',
        string="Country",
        tracking=True)
    user_id = fields.Many2one('res.user',
        string="Responsable",
        tracking=True)
    employee_id = fields.Many2one(
        'hr.employee',
        string="Operator notice",
        tracking=True)
    employee_greasing_id = fields.Many2one(
        'hr.employee',
        string="Greasing operator",
        tracking=True)
    guard_zone = fields.Char(string="Guard zone", tracking=True)
    route_ids = fields.Many2many(
        'res.partner.routes',
        'route_partner_rel',
        string="Routes")
    product_line_ids = fields.One2many(
        'res.partner.zones.lines',
        'zone_id',
        string="Gadgets",
        tracking=True)
    employee_greasing_code = fields.Char(
        string="Cod.Ope.",
        tracking=True)
    employee_notice_code = fields.Char(
        string="Cod.Ope.",
        tracking=True)


    # Ejecutar Secuencia 
    @api.model
    def create(self, vals):
        if vals.get('code', 'New') == 'New':
            vals['code'] = self.env['ir.sequence'].next_by_code('zone') or 'New'
        result = super(ResPartnerZones, self).create(vals)
        return result


class ResPartnerZonesLines(models.Model):
    _name = 'res.partner.zones.lines'
    _inherit = 'mail.thread'
    _description = 'Zones lines'

    zone_id = fields.Many2one(
        'res.partner.zones',
        string="Zone",
        tracking=True)
    product_id = fields.Many2one(
        'product.template',
        string="Gadgets",
        tracking=True)
