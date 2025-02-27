{
    'name': 'Odoo Hiscox Integration',
    'version': '1.0',
    'category': 'Custom',
    'summary': 'Integration with Hiscox API and QR Code generation',
    'description': 'Module to manage customer applications, create a QR code, and integrate with Hiscox API.',
    'author': 'Ritik Patil',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/hiscox_case_views.xml',
    ],
    'installable': True,
    'application': True,
}
