# -*- coding: utf-8 -*-
{
    'name': "Impresión de Ticket desde Presupuestos",

    'summary': """
        Agrega opcion de imprimir ticket en sale order""",

    'description': """
        Agrega opcion de imprimir ticket en sale order
    """,

    'author': "Link Tech",
    'website': "https://www.linktechsv.com/",

    'category': 'Sale',
    'version': '0.1',

    'depends': ['base', 'sale', 'sale_management'],

    'data': [
        'views/templates.xml',
        #'views/link_tech_ticket_print_sale_order.xml',
        'reports/report.xml',
    ],
}
