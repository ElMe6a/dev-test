# -*- coding: utf-8 -*-

from odoo import fields, models

class Peliculas(models.Model):
    _name = 'cvp.cvp_peliculas'
    #_inherit = 'cvp.peliculas'
    
    imagen = fields.Binary(string = 'Imagen')
    titulo =  fields.Char(string = 'Titulo de la Pelicula', required = True)
    fecha_lanzamiento = fields.Date(string ='Fecha de Lanzamiento') #Falta el Constraint
    longuitud_minutos = fields.Datetime(string = 'Minutos de Pelicula')
    director_id = fields.Many2one('res.users' ,'cdirector_id', ondelete='cascade') # Relacion * - 1
    #actores_id = fields.One2many('res.users','cactores_id')
    #actores_id = fields.One2many('res.users', 'cactores_id') # Relacion 1 - *
    #producto_asociado Crear una realcion *-1 a la tabla compras
    sinopsis = fields.Text(string = 'Sinopsis', required = True)
    costo_pelicula = fields.Float(string = 'Costo', required = True)
    iva = fields.Float(string = 'Iva',required = True)
    #total, este campo se calcula / checa en el word