# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class open__academy(models.Model):
#     _name = 'open__academy.open__academy'
#     _description = 'open__academy.open__academy'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
