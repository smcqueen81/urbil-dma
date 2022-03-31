from odoo import models, fields, api
import logging

class WizardSaleOrderType(models.TransientModel):
    _name = 'wizard.sale.order.type'

    sale_order_id = fields.Many2one('sale.order', 'Sale order')
    sale_type_id = fields.Many2one('sale.order.type', 'Sale order Type')
    
    
    def accept_task_type_sale(self):
        for record in self:
            project_model = self.env['project.project'].search([('sale_order_id','=',record.sale_order_id.id)])
            if project_model:
                for p in project_model:
                    p.write({
                        'type_ids': record.sale_type_id.project_stage_ids.ids,
                        'task_ids': record.sale_type_id.project_task_ids.ids
                    })
                    
            else:
                new_project = self.env['project.project'].create({
                            'name': 'PROJECT'+record.sale_order_id.name,
                            'sale_type_origin_id': record.sale_type_id.id,
                            'type_ids': record.sale_type_id.project_stage_ids.ids,
                            'task_ids': record.sale_type_id.project_task_ids.ids
                        })