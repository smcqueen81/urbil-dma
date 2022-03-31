{
    'name': 'SAT COMPANIES',

    'version': '14.0.1',

    'author': "Process Control",

    'contributors': ['Luis Felipe Paternina'],

    'website': "https://www.processcontrol.es/",

    'category': 'Maintenance',

    'depends': [

        'sale_management',
        'contacts',
        'account_accountant',
        'account',
        'sale_subscription',
        'crm',
        'base',
        'base_automation',
        'hr_holidays',
        'sat_companies_stock',

    ],

    'data': [
       
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/res_company.xml',
        'views/account_move_line.xml',
        'reports/invoice.xml',
        'reports/inherit_sale_order.xml',
                   
    ],
    'installable': True
}

