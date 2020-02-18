# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Sale_Order_Inherit(models.Model):
    _inherit = 'sale.order'
    img_include = fields.Boolean(string="Product Images", help="Show Images in Quotation Print")

class Customer_inherit(models.Model):
    _inherit = 'res.partner'

    name_ar = fields.Char("Name in Arabic ")


class Product_inherit(models.Model):
    _inherit = 'product.product'

    name_ar = fields.Char("Name in Arabic")


class Product_uom_inherit(models.Model):
    _inherit = 'product.uom'

    name_ar = fields.Char("Name in Arabic")

class Company_Logo_Secondary(models.Model):
    _inherit = 'res.company'

    logo_2 = fields.Binary(string="Secondary Logo",  )


