# -*- coding: utf-8 -*-
{
    'name': "link_tech_ticket_print_sale_order",

    'summary': """
        Agrega opcion de imprimir ticket en sale order""",

    'description': """
        Agrega opcion de imprimir ticket en sale order
    """,

    'author': "Link Tech",
    'website': "https://www.linktechsv.com/",

    'category': 'Sale',
    'version': '0.1',

    'depends': ['base', 'sale'],

    'data': [
        'views/templates.xml',
        'reports/report.xml'
    ],
}
