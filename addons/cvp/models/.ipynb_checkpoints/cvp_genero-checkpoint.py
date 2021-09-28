from odoo import models, fields, api

class Generos(models.Model):
    _name = 'cvp.generos'
    
    nombre_genero = fields.Char(string = 'Genero',required = True)
    descripcion = fields.Text(string = 'Descripcion', required = True)
    #relacion de la tabla
    pelicula_ids = fields.Many2many('cvp.peliculas', 'genero_ids', string = 'pelicula')