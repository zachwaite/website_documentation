# -*- coding: utf-8 -*-
# © 2018 Waite Perspectives, LLC - Zach Waite
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import http, _
from odoo.http import request

from odoo.addons.website_portal.controllers.main import website_account


class WebsiteAccount(website_account):
    def _prepare_portal_layout_values(self):
        values = super(WebsiteAccount, self)._prepare_portal_layout_values()
        document_category_count = request.env['document.page'].search_count([
            ('type', '=', 'category'),
        ])
        document_page_count = request.env['document.page'].search_count([
            ('type', '=', 'content'),
        ])
        values.update({
            'document_category_count': document_category_count,
            'document_page_count': document_page_count,
        })
        return values

    @http.route(['/my/documentation_categories',
                 '/my/documentation_categories/page/<int:page>'
                ], type='http', auth='user', website=True)
    def my_documentation_categories(self, page=1, **kw):
        values = self._prepare_portal_layout_values()
        DocumentPage = request.env['document.page']

        pager  = request.website.pager(
            url="/my/documentation_categories",
            url_args={},
            total=values['document_category_count'],
            page=page,
            step=self._items_per_page,
        )

        categories = DocumentPage.search([
            ('type', '=', 'category'),
        ], limit=self._items_per_page, offset=pager['offset'])
        values.update({
            'categories': categories,
            'pager': pager,
        })
        return request.render('website_documentation.my_documentation_categories', values)

    @http.route(['/my/documentation_categories/<model("document.page"):document_page>'],
                type='http', auth='user', website=True)
    def my_document_category(self, page=1, document_page=None, **kw):
        # remember a category is a page
        return request.render('website_documentation.my_category', {'category': document_page})

    @http.route(['/my/documentation_pages/', '/my/documentation_pages/page/<int:page>'],
                type='http', auth='user', website=True)
    def my_document_pages(self, page=1, category=None, **kw):
        values = self._prepare_portal_layout_values()

        pager  = request.website.pager(
            url="/my/documentation_pages",
            url_args={},
            total=values['document_page_count'],
            page=page,
            step=self._items_per_page,
        )

        domain = [('type', '=', 'content')]
        if category is not None:
            domain.append(
                ('parent_id', '=', int(category))
            )

        documentation_pages = request.env['document.page'].search(domain)

        values.update({
            'documentation_pages': documentation_pages,
            'pager': pager,
        })

        return request.render('website_documentation.my_documentation_pages', values)

    @http.route(['/my/documentation_page/<model("document.page"):page>'],
                type='http', auth='user', website=True)
    def my_documentation_page(self, page=None, **kw):
        values = self._prepare_portal_layout_values()
        values.update({
            'documentation_page': page,
            'user': request.env.user,
        })
        return request.render('website_documentation.my_documentation_page', values)
