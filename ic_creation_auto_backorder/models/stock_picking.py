# -*- coding: utf-8 -*-
# Part of Idealis Consulting. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def action_generate_backorder_wizard(self):
        backorder = self.env['stock.backorder.confirmation'].create({'pick_ids': [(4, p.id) for p in self]})
        if self.picking_type_id.code == 'incoming' and self.partner_id:
            if self.partner_id.auto_backorder_receipt:
                if self.partner_id.auto_backorder_receipt == 'auto_creation':
                    backorder.process()
                elif self.partner_id.auto_backorder_receipt == 'auto_cancel':
                    backorder.process_cancel_backorder()
                else:
                    return super(StockPicking, self).action_generate_backorder_wizard()
        elif self.picking_type_id.code == 'outgoing' and self.partner_id:
            if self.partner_id.auto_backorder_delivery:
                if self.partner_id.auto_backorder_delivery == 'auto_creation':
                    backorder.process()
                elif self.partner_id.auto_backorder_delivery == 'auto_cancel':
                    backorder.process_cancel_backorder()
                else:
                    return super(StockPicking, self).action_generate_backorder_wizard()
        else:
            if self.picking_type_id.backorder_automation == 'auto_creation':
                backorder.process()
            elif self.picking_type_id.backorder_automation == 'auto_cancel':
                backorder.process_cancel_backorder()
            else:
                return super(StockPicking, self).action_generate_backorder_wizard()
