# -*- coding: utf-8 -*-

{
    'name': "Tax Amount on Lines",
    'version': '15.0',
    'category': "Accounting",
    'summary': """Tax Amount on Lines""",
    'author': 'Amal Salah',
    'company': 'For Promate Technologies',
    'depends': ['base','sale'],
    'data': [


        'views/sale_order_line.xml',
        'views/account_move_line.xml',
        ],


    'installable': True,
    'auto_install': False,
    'application': False,
}
