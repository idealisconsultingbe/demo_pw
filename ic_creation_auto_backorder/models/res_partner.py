# -*- coding: utf-8 -*-
# Part of Idealis Consulting. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

BACKORDER_AUTOMATION = [('auto_creation', 'Automatic Creation'), ('auto_cancel', 'Automatic Cancellation'),
                        ('manual', 'Manual')]


class ResPartner(models.Model):
    _inherit = 'res.partner'

    auto_backorder_receipt = fields.Selection(selection=BACKORDER_AUTOMATION, default='manual',
                                              string='Backorder Automation for Reception')
    auto_backorder_delivery = fields.Selection(selection=BACKORDER_AUTOMATION, default='manual',
                                               string='Backorder Automation for Delivery')
