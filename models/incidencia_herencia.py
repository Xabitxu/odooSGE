from odoo import models, fields

class IncidenciaHerencia(models.Model):
    _inherit = 'sge.incidencia'

    prioridad = fields.Selection([
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
        ('critica', 'Crítica'),
    ], string='Prioridad', default='media')