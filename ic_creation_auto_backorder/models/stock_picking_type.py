# -*- coding: utf-8 -*-
# Part of Idealis Consulting. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class StockPickingType(models.Model):
    _inherit = 'stock.picking.type'

    backorder_automation = fields.Selection(string='Backorder Automation',
                                            selection=[('auto_creation', 'Automatic Creation'),
                                                       ('auto_cancel', 'Automatic Cancellation'),
                                                       ('manual', 'Manual')])
