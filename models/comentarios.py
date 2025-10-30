from odoo import fields, models

class Comentarios(models.Model):
    _name = 'sge.comentarios'
    _description = 'Comentarios'

    contenido = fields.Text(string='Contenido')
    fecha = fields.Date(string='Fecha', required=True)
