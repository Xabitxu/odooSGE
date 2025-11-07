from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Encuesta(models.Model):
    _name = 'sge.encuesta'
    _description = 'Encuesta de satisfacción sobre la incidencia'

    name = fields.Char(string='Título', required=True)

    incidencia_id = fields.One2many('sge.incidencia', 'encuesta_id', string='Incidencia (1-1)')

    puntuacion = fields.Selection([
        ('1', 'Muy mala'),
        ('2', 'Mala'),
        ('3', 'Normal'),
        ('4', 'Buena'),
        ('5', 'Excelente')
    ], string='Puntuación', required=True)

    observaciones = fields.Text(string='Observaciones')

    @api.constrains('incidencia_id')
    def _check_one2one(self):
        for record in self:
            if len(record.incidencia_id) > 1:
                raise ValidationError("Cada encuesta solo puede estar asignada a una única incidencia.")
