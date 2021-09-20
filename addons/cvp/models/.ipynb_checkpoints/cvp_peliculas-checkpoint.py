from odoo import models, fields, api

class peliculas(models.Model):
    _name = 'cvp.peliculas'
    
    imagen = fields.Binary(string = 'Imagen', required = True)
    titulo = fields.Char(string = 'Titulo de la pelicula', required = True)
    fecha_lanzamiento = fields.Date(string = 'Fecha de lanzamiento')
    longitud_minutos = fields.DateTime(strings = 'Minutos de la pelicula')
    # director = fields.Many2one('res.users', required = True, string = 'Director')
    # actores = fields.Many2one('res.users', required = True, string = ' Actores')
    # producto_asociado = fields.Char(string = 'Producto') seria char o many2one?  
    sinopsis = fields.Text(string = 'Sinopsis', required = True)
    costo_pelicula = fields.Float(string = 'Costo', (8,2), required = True)
    iva = fields.Float(string = 'Iva',required = True)
    total = fields.Float('Total', compute = '_get_total')
    
    #relacion de la tabla
 #  genero_ids = fields.Many2many('cvp.generos', string = 'generos')
 #  studio_id = fields.Many2one('cvp.studio', string = 'studios')
    
    #para computar el total pero falta cambio
 #   @api.depends('costo_pelicula', 'iva')
 #   def _get_total(self):
 #       for peliculas self:
 #       peliculas.total = 0