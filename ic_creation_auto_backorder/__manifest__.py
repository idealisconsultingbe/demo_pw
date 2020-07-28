# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2020 Idealis Consulting.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Backorder Automatic Creation',
    'version': '13.0.1.0.0',
    'author': 'Idealis Consulting',
    'website': 'http://www.idealisconsulting.com',
    'category': 'stock',
    'sequence': 8,
    'images': [],
    'depends': ['stock'],

    'description':
        """
        A flag on the Operation Type will determine if a picking's backorder will be automatically created, or not.
        """,
    'data': [
        'views/stock_picking_type_views.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
