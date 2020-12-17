# -*- coding: utf-8 -*-
{
    'name': "my_module_JC_Fusion",

    'summary': """
        Este es un módulo de prueba para JC Fusion""",

    'description': """
        JC Fusion - Módulo de prueba
    """,

    'author': "Enmanuel Feliz E",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
