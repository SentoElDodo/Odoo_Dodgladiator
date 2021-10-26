# -*- coding: utf-8 -*-
# from odoo import http


# class Dodcity(http.Controller):
#     @http.route('/dodcity/dodcity/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dodcity/dodcity/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dodcity.listing', {
#             'root': '/dodcity/dodcity',
#             'objects': http.request.env['dodcity.dodcity'].search([]),
#         })

#     @http.route('/dodcity/dodcity/objects/<model("dodcity.dodcity"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dodcity.object', {
#             'object': obj
#         })
