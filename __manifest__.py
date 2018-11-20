{
    'name': 'Portal Documentation',

    'summary': "Website portal for Document Pages",

    'description': """
Portal access for document pages
==================================

* Create and manage document pages as data records
* Changes to document pages are captured when the module updates (assuming noupdate="0")
* Document categories and pages are indexed by sequence
""",

    'author': 'Waite Perspectives, LLC - Zach Waite',
    'website': 'https://www.waiteperspectives.com',

    'category': 'Website',
    'version': '0.1',

    'depends': [
        'website_portal',
        'document_page',
    ],

    'data': [
        'views/views.xml',
        'views/templates.xml',
    ],

    'demo': [
        'data/demo_pages.xml',
    ],
}

