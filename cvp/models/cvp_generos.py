# -*- coding: utf-8 -*-

from odoo import fields, models

class Generos(models.Model):
    _name = 'cvp.cvp_generos'
    #_inherit = 'cvp.generos'
    
    #generos_id = fields.Many2many('cvp.peliculas', 'titulo', 'sinopsis', string = 'Campo Many2many')
    nombre = fields.Char(string = 'Nombre del Genero',required = True)
    descripcion = fields.Text(string = 'Descripcion del genero', required = True)
    