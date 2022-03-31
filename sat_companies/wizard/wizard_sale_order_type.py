from odoo import models, fields, api
import logging

class WizardSaleOrderType(models.TransientModel):
    _name = 'wizard.sale.order.type'

    name = fields.Char('')
    sale_order_id = fields.Many2one('sale.order', 'Sale order')
    sale_type_id = fields.Many2one('sale.order.type', 'Sale order Type')
    is_new_project = fields.Boolean('Is a project existing ?')
    project_id = fields.Many2one('project.project', 'Project')
    
    
    
    def accept_task_type_sale(self):
        for record in self:
            #project_model = self.env['project.project'].search([('sale_order_id','=',record.sale_order_id.id)])
            if record.is_new_project == True:
                for p in record.project_id:
                    p.write({
                        'type_ids': record.sale_type_id.project_stage_ids.ids,
                        'task_ids': record.sale_type_id.project_task_ids.ids
                    })
                    
            else:
                self.env['project.project'].create({
                    'name': record.name,
                    'sale_type_origin_id': record.sale_type_id.id,
                    'type_ids': record.sale_type_id.project_stage_ids.ids,
                    'task_ids': record.sale_type_id.project_task_ids.ids
                })
            record.sale_order_id.action_confirm()