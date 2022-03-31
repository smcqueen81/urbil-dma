# -*- coding: utf-8 -*-
#╔══════════════════════════════════════════════════════════════════════╗
#║                                                                      ║
#║                  ╔═══╦╗       ╔╗  ╔╗     ╔═══╦═══╗                   ║
#║                  ║╔═╗║║       ║║ ╔╝╚╗    ║╔═╗║╔═╗║                   ║
#║                  ║║ ║║║╔╗╔╦╦══╣╚═╬╗╔╬╗ ╔╗║║ ╚╣╚══╗                   ║
#║                  ║╚═╝║║║╚╝╠╣╔╗║╔╗║║║║║ ║║║║ ╔╬══╗║                   ║
#║                  ║╔═╗║╚╣║║║║╚╝║║║║║╚╣╚═╝║║╚═╝║╚═╝║                   ║
#║                  ╚╝ ╚╩═╩╩╩╩╩═╗╠╝╚╝╚═╩═╗╔╝╚═══╩═══╝                   ║
#║                            ╔═╝║     ╔═╝║                             ║
#║                            ╚══╝     ╚══╝                             ║
#║                  SOFTWARE DEVELOPED AND SUPPORTED BY                 ║
#║                ALMIGHTY CONSULTING SOLUTIONS PVT. LTD.               ║
#║                      COPYRIGHT (C) 2016 - TODAY                      ║
#║                      https://www.almightycs.com                      ║
#║                                                                      ║
#╚══════════════════════════════════════════════════════════════════════╝
{
    'name': 'Invoice Global Discounts',
    'category': 'Accounting',
    'version': '1.0.2',
    'author' : 'Almighty Consulting Solutions Pvt. Ltd.',
    'support': 'info@almightycs.com',
    'website': 'https://www.almightycs.com',
    'license': 'OPL-1',
    'summary': """Apply Global Discounts on Invoices based on fixed amounts and percentage""",
    'description': """Apply Global Discounts on Invoices based on fixed amounts and percentage.
    Global Discounts
    Global Discount
    Fixed Amount Discount
    Discount on Total
    Discount in Invoice
    Global Discount in Invoice""",
    'depends': ['account'],
    'data': [
        'views/invoice_view.xml',
        'views/res_config_view.xml',
    ],
    'images': [
        'static/description/discount_cover_almightycs_turkesh.png',
    ],
    'installable': True,
    'auto_install': False,
    'price': 14,
    'currency': 'EUR',
}


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
