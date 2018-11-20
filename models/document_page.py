# -*- coding: utf-8 -*-
# © 2018 Waite Perspectives - Zach Waite
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, api, _


class DocumentPage(models.Model):
    _inherit = 'document.page'
    _order = 'sequence'

    sequence = fields.Integer(
        help=_("Used to sort documents in the table of contents"),
        string=_("Sequence"),
        default=16,
    )

    document_count = fields.Integer(
        string=_("Document Count"),
        compute="_compute_document_count",
    )

    @api.multi
    @api.depends('child_ids')
    def _compute_document_count(self):
        for doc in self:
            doc.document_count = len(doc.child_ids)

