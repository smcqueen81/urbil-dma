# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class ResUsers(models.Model):
    _inherit = 'res.users'

    route_id = fields.Many2one(
        'res.partner.routes',
        string="Normal route",
        tracking=True)
    route_type_id = fields.Many2one(
        'res.partner.routes',
        string="Guard route",
        tracking=True)
    product_ids = fields.Many2many(
        'product.template',
        string="Gadgets")
    zones_ids = fields.Many2many(
        'res.partner.zones',
        compute="compute_zones_user",
        string="Zones")
    routes_ids = fields.Many2many(
        'res.partner.routes',
        compute="compute_routes_user",
        string="Routes")

    def compute_products_user(self):
        product = self.env['product.template'].search([('user_id','=',self.id)])
        if product:
            self.product_ids = product.ids
        else:
            self.product_ids = False

    def compute_zones_user(self):
        zones_model = self.env['res.partner.zones'].search([])
        if zones_model:
            ids_zones = []
            for record in zones_model:
                if self.id in record.users_ids.ids:
                    ids_zones.append(record.id)
                
                if ids_zones:
                    self.zones_ids = ids_zones
                
                else:
                    self.zones_ids = False
        else:
            self.zones_ids = False
        
    def compute_routes_user(self):
        routes_model = self.env['res.partner.routes'].search([])
        if routes_model:
            ids_routes = []
            for record in routes_model:
                if self.id in record.users_ids.ids:
                    ids_routes.append(record.id)
                
                if ids_routes:
                    self.routes_ids = ids_routes
                
                else:
                    self.routes_ids = False
        else:
            self.routes_ids = False
    
