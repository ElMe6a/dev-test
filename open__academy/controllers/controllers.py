# -*- coding: utf-8 -*-
# from odoo import http


# class OpenAcademy(http.Controller):
#     @http.route('/open__academy/open__academy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/open__academy/open__academy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('open__academy.listing', {
#             'root': '/open__academy/open__academy',
#             'objects': http.request.env['open__academy.open__academy'].search([]),
#         })

#     @http.route('/open__academy/open__academy/objects/<model("open__academy.open__academy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('open__academy.object', {
#             'object': obj
#         })
