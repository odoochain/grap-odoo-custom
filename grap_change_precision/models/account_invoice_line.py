# coding: utf-8
# Copyright (C) 2014 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from openerp import fields, models
from openerp.addons import decimal_precision as dp


class AccountInvoiceLine(models.Model):
    _inherit = "account.invoice.line"

    price_unit = fields.Float(
        digits=dp.get_precision("GRAP Purchase Unit Price")
    )

    discount = fields.Float(
        digits=dp.get_precision("GRAP Purchase Unit Discount")
    )
