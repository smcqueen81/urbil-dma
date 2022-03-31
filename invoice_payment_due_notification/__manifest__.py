# -*- coding: utf-8 -*-
{
    'name': "Invoice payment due notification",

    'summary': """
        Send specific users notifications on invoice payment due.
        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Alberto Touriñán - Process Control",
    'website': "https://www.processcontrol.es",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account_reports',],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/invoice_payment_due_data.xml',
        'views/res_config_settings_views.xml',
        'views/account_move_views.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
