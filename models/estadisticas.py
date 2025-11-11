from odoo import models, fields
from datetime import datetime

class Estadisticas(models.Model):
    _name = 'sge.estadisticas'
    _description = 'Estadísticas de incidencias'

    fecha = fields.Date(string='Fecha', required=True)
    total_incidencias = fields.Integer(string='Total de incidencias', readonly=True)
    incidencias_finalizadas = fields.Integer(string='Incidencias finalizadas', readonly=True)
    tiempo_promedio_resolucion = fields.Float(string='Tiempo promedio de resolución (horas)', readonly=True)