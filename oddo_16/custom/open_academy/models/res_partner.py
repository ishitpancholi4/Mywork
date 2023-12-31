from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    instructor = fields.Boolean(string='Instructor', default=False)
    session_ids = fields.Many2many('openacademy.session', string='Attended Sessions', readonly=True)
