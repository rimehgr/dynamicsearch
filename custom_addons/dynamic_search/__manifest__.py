
{
    'name': 'Shazler Product Search',
    'version': '1.0',
    'summary': 'Dynamic search',
    'category': 'Product',
    'sequence': -100,
    'author': 'Rimeh Grissiaa',
    'depends': ['base', 'product', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/product.xml',
        'views/menu.xml',

    ],

    'js': [
        'static/src/js/product_search.js',

    ],

    'installable': True,
    'application': False,
    'assets': {},
    'license': 'LGPL-3',
}
