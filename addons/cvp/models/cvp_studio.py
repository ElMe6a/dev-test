from odoo import models, fields, api

class Studio(models.Model):
    _name = 'cvp.studio'

    nombre_studio = fields.Char(string = 'Nombre del Studio', required = True)
    #relaciones entre tablas
    pelicula_id = fields.One2many('cvp.peliculas', 'studio_id', string = 'pelicula')