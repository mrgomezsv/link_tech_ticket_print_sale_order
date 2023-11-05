# -*- coding: utf-8 -*-

from odoo import api, fields, models
from datetime import datetime


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    budget_number = fields.Char('Número de Presupuesto')

    # Este método se ejecuta antes de imprimir el informe
    def prepare_report(self):
        # Obtén la fecha y hora actual
        current_datetime = datetime.now()

        # Suponiendo que 'self' es la instancia de tu objeto sale.order
        self.print_date = current_datetime
