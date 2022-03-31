{
    'name': 'SAT COMPANIES SALE',

    'version': '14.0.1',

    'author': "Process Control",

    'contributors': ['Luis Felipe Paternina'],

    'website': "https://www.processcontrol.es/",

    'category': 'Sale',

    'depends': [

        'sale_management',
        'crm',
        'website',
        'sat_companies_project',
        'base_automation',
        'sale_subscription',
        'sat_companies',
        'sat_companies_partner',

    ],

    'data': [
       
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/sale_type_service_views.xml',
        'views/crm_lead.xml',
        'views/crm_lead_type.xml',
        'views/sale_order.xml',
        'views/crm_stage.xml',
        'templates/sale_contract_report_web_template.xml',
        'templates/sale_contract_mail_template.xml',
        'templates/template_sale_sample.xml',
        'reports/sale_order_maintenance_offer.xml',
        'reports/sale_order_suspension_contract.xml',
        'reports/sale_order_contract.xml',
        'reports/sale_order_client_documentation.xml',
        'data/sale_order_sent_email_data.xml',
        'data/sale_order_maintenance_offer.xml',
        'data/crm_lead_opportunity_notify.xml',
        'data/base_automatization.xml',
        'data/mail_contract.xml',
        'data/send_email_max_days.xml',
        
    ],
    'installable': True
}
