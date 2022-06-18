
from odoo import api, fields, models

class SaleOrderLine(models.Model):
    _inherit = 'account.move.line'


    tax_amount = fields.Float(compute='_compute_tax_amount')

    @api.depends('tax_ids','price_total')
    def _compute_tax_amount(self):
        for record in self:
            record.tax_amount = record.price_total - record.price_subtotal