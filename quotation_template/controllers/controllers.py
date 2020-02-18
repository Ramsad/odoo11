# -*- coding: utf-8 -*-
from openerp import http

# class QuotationTemplate(http.Controller):
#     @http.route('/quotation_template/quotation_template/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/quotation_template/quotation_template/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('quotation_template.listing', {
#             'root': '/quotation_template/quotation_template',
#             'objects': http.request.env['quotation_template.quotation_template'].search([]),
#         })

#     @http.route('/quotation_template/quotation_template/objects/<model("quotation_template.quotation_template"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('quotation_template.object', {
#             'object': obj
#         })