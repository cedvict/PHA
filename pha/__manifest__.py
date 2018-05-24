# -*- coding: utf-8 -*-
{
    'name': 'PHA',
    'version': '0.1',
    'category': 'Product Management',

    'summary': 'PHA module specifique ',
    'sequence': 1,
    'author': "Cadrinsitu",
    'website': "http://www.cadrinsitu.com",


    'depends': ['base','sale','sale_stock','pha_partner_fax','stock','account','purchase','ci_account_desc','stock_location'],
    'data': [
        'views/report_templates.xml',
        'views/account_invoice_view.xml',
        'views/res_company_view.xml',
        'views/product_template_view.xml',
        'views/stock_move_view.xml',
        'reports/external_templates.xml',
        'reports/invoice_report.xml',
        'reports/sale_order.xml',
        'reports/invoice.xml',
        'reports/purchase_quotation_templates.xml',
        'reports/purchase_order_templates.xml',
        'reports/report_deliveryslip.xml',
    ],

    'installable': True,
}
