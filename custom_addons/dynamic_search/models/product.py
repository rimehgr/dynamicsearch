from odoo import models, fields, api


class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        args = args or []
        domain = ['|', '|',
                  ('name', operator, name),
                  ('reference', operator, name),
                  ('description', operator, name)]
        return super(ProductProduct, self).name_search(name, args=args, operator=operator, limit=limit)
