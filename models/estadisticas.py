from odoo import fields, models


class Estadisticas(models.Model):
    _name = 'sge.estadisticas'
    _description = 'Estadísticas de incidencias'

    fecha = fields.Date(string='Fecha', required=True)
    total_incidencias = fields.Integer(string='Total de incidencias', compute='_compute_totales', store=True)
    incidencias_finalizadas = fields.Integer(string='Incidencias finalizadas', compute='_compute_totales', store=True)
    tiempo_promedio_resolucion = fields.Float(string='Tiempo promedio de resolución (horas)',compute='_compute_totales', store=True)

