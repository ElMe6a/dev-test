# -*- coding: utf-8 -*-

from odoo import models, fields, api


#class cvp(models.Model):
 #   _name = 'cvp.cvp'
 #  _description = 'cvp.cvp'

 #   name = fields.Char()
 #   value = fields.Integer()
 #   value2 = fields.Float(compute="_value_pc", store=True)
 #   description = fields.Text()

 #   @api.depends('value')
 #   def _value_pc(self):
 #       for record in self:
 #           record.value2 = float(record.value) / 100
                
class peliculas(models.Model):
    _name = 'cvp.cvp_peliculas'
    
    imagen = fields.Binary(string = 'Imagen', required = True)
    titulo = fields.Char(string = 'Titulo de la pelicula', required = True)
    fecha_lanzamiento = fields.Date(string = 'Fecha de lanzamiento')
    longitud_minutos = fields.DateTime(strings = 'Minutos de la pelicula')
    director = fields.Many2one('res.users', required = True, string = 'Director')
    actores = fields.Many2one('res.users', required = True, string = ' Actores')
    # producto_asociado = fields.Char(string = 'Producto') seria char o many2one?  
    sinopsis = fields.Text(string = 'Sinopsis', required = True)
    costo_pelicula = fields.Float(string = 'Costo', (8,2), required = True)
    iva = fields.Float(string = 'Iva',required = True)
    total = fields.Float('Total', compute = '_get_total')
    
    #relacion de la tabla
    genero_ids = fields.Many2many('cvp.cvp_generos', string = 'generos')
    studio_id = fields.Many2one('cvp.cvp_studio', string = 'studios')
    
    #para computar el total pero falta cambio
    @api.depends('costo_pelicula', 'iva')
    def _get_total(self):
        for peliculas self:
        peliculas.total = 0
  
class generos(models.Model)
    _name = 'cvp.cvp_generos'
    
    nombre_genero = fields.Char(string = 'Genero',required = True)
    descripcion = fields.Text(string = 'Descripcion', required = True)
    #relacion de la tabla
    pelicula_ids = fields.Many2many('cvp.peliculas', 'genero_ids', string = 'pelicula')
    
class studio(models.Model)
    _name = 'cvp.cvp_studio'

    nombre_studio = fields.Char(string = 'Nombre del Studio', required = True)
    #relaciones entre tablas
    pelicula_id = fields.One2many('cvp.peliculas', 'studio_id' string = 'pelicula')