# -*- coding: utf-8 -*-
# Part of Idealis Consulting. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class StockPickingType(models.Model):
    _inherit = 'stock.picking.type'

    auto_backorder = fields.Boolean(string='Automatic Backorder')
