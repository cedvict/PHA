# -*- coding: utf-8 -*-
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import http


class Main(http.Controller):

    @http.route('/web/map_theme', type='json', auth='user')
    def map_theme(self):
        ICP = http.request.env['ir.config_parameter'].sudo()
        theme = ICP.get_param('google_maps_theme', default='default')
        res = {'theme': theme}
        return res
