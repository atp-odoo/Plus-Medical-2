# -*- coding: utf-8 -*-
{
    'name': 'Sale Order Undilivered (List View, Form View, Search View)',
    
    'author' : 'Softhealer Technologies',
    
    'website': 'https://www.softhealer.com',
    
    'version': '11.0.3',
    
    'support': 'support@softhealer.com',
    
    'category': 'Sales',

    'summary': 'This module useful to show sale order lines products and other information related to it.',

    'description': """This module useful to show sale order lines products and other information related to it.""",
    
    'depends': ['sale_management'],
    
    'data': [
        'views/sale_order_line.xml',
    ],
    
    'images': ['static/description/background.png', ],
                  
    'auto_install': False,
    'installable' : True,
    'application': True,
        
    "price": 25,
    "currency": "EUR"        
}