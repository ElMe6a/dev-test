# -*- coding: utf-8 -*-

from odoo import fields, models

class Studio(models.Model):
    _name = 'cvp.cvp_studio'
    #_inherit = 'cvp.studio'
    
    #studio_id = fields.One2many('cvp.peliculas', string = 'Campo One2many')
    nombre = fields.Char(string = 'Nombre del Studio', required = True)