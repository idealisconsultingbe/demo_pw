# -*- coding: utf-8 -*-
# Part of Idealis Consulting. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def action_generate_backorder_wizard(self):
        backorder = self.env['stock.backorder.confirmation'].create({'pick_ids': [(4, p.id) for p in self]})
        if self.picking_type_id.auto_backorder:
            backorder.process()
        else:
            backorder.process_cancel_backorder()
        super(StockPicking, self).action_generate_backorder_wizard()
