# -*- coding: utf-8 -*-
{
    'name': "cvp",

    'summary': """
        Ejercicio 3
        """,

    'description': """
        módulo en el cual se registran películas para comprar películas y vender peliculas
    """,

    'author': "Michael",
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
        #'views/views.xml',
        'views/templates.xml',
        'views/vista_peliculas.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    
    #INDICAMOS QUE ES UNA APLICACION
    #'application' = True
}
