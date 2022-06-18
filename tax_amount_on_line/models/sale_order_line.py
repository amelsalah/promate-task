
from odoo import api, fields, models

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'


    tax_amount = fields.Float(compute='_compute_tax_amount')

    @api.depends('tax_id','price_total')
    def _compute_tax_amount(self):
        for record in self:
            record.tax_amount = record.price_total - record.price_subtotal
            return {
            'type': 'ir.actions.client',
            'tag': 'reload',
                }