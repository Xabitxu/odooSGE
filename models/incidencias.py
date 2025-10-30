from odoo import fields, models

class Incidencias(models.Model):
    _name = 'sge.comentarios'
    _description = 'Comentarios'

    titulo = fields.Char(string='Titulo')
    descripcion = fields.Text(string='Descripcion')
    fecha_creacion = fields.Date(string='Fecha Creacion', required=True)
    estado_actual = fields.Char(string='Estado actual')
