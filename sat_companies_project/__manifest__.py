{
    'name': 'SAT COMPANIES PROJECT',

    'version': '14.0.1',

    'author': "Process Control",

    'contributors': ['Luis Felipe Paternina'],

    'website': "https://www.processcontrol.es/",

    'category': 'Project',

    'depends': [

        'sale_management',
        'project',
        'industry_fsm',
        'sat_companies_stock',
        'sat_companies_industry',
        'base_automation',

    ],

    'data': [
       
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/sale_order_type.xml',
        'views/res_partner.xml',
        'views/project_task.xml',
        'views/sale_order.xml',
        'views/project_task_categ_udn_ot.xml',
        'views/stock_picking.xml',
        'views/project_project_view.xml',
        'wizard/wizard_sale_order_type_view.xml',
        'data/project_template_inspection_notice.xml',
        'data/project_template_new_task.xml',
        'data/action_automated_new_field_service.xml',
        #'data/sale.order.type.csv',
        
    ],
    'installable': True
}

