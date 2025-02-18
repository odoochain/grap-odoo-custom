# Copyright (C) 2022 - Today: GRAP (http://www.grap.coop)
# @author: Quentin DUPONT (quentin.dupont@grap.coop)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models

from odoo.addons import decimal_precision as dp


class BomPrintPurchaseListWizardLine(models.TransientModel):
    _name = "bom.print.purchase.list.wizard.line"
    _description = (
        "Wizard line for printing purchase list from selected bill of materials"
    )

    # Columns Section
    wizard_id = fields.Many2one(comodel_name="bom.print.purchase.list.wizard")

    bom_id = fields.Many2one(comodel_name="mrp.bom", string="Bill Of Material")

    currency_id = fields.Many2one(
        comodel_name="res.currency",
        related="bom_id.currency_id",
    )

    bom_description = fields.Char(
        string="Description", compute="_compute_bom_description"
    )

    bom_product_qty = fields.Float(string="BoM Qty", related="bom_id.product_qty")

    bom_uom_id = fields.Many2one(
        related="bom_id.product_uom_id",
        string="UoM",
    )

    quantity = fields.Float(
        string="Desired Quantity",
        default=1,
    )

    wizard_line_subtotal = fields.Float(
        string="Cost",
        digits=dp.get_precision("Product Price"),
        compute="_compute_wizard_line_subtotal",
    )

    @api.depends("bom_id")
    def _compute_bom_description(self):
        for line in self.filtered(lambda x: x.bom_id):
            line.bom_description = line.bom_id.description_short

    @api.depends("bom_id", "quantity")
    def _compute_wizard_line_subtotal(self):
        # standard_price_total is already divide for product unit
        for line in self.filtered(lambda x: x.bom_id):
            line.wizard_line_subtotal = line.bom_id.standard_price_total * line.quantity
