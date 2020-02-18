# -*- coding: utf-8 -*-
{
    'name': "quotation_template",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Ramsad PV",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/paper_format.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/sale_quatation_report.xml',
        'views/sale_quatation_report_view.xml',
        'views/sale_quatation_report_AR_view.xml',

    ],

}