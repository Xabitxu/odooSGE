from odoo import fields, models


class Encuesta(models.Model):
    _name = 'sge.encuesta'
    _description = 'Encuesta de incidencias'
    id_incidencia = fields.One2one(
        'incidencia.incidencia',
        string = 'Incidencia',
        required = True
    )
    puntuacion = fields.Integer(string='Puntuación', required=True)
    comentario = fields.Text(string='Comentario')
    fecha_respuesta = fields.Date(string='Fecha de Respuesta', default=fields.Date.today)
    id_empleado = fields.One2one('incidencia.id_empleado_origen', string='Empleado', required=True)
