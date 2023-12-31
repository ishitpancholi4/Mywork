from odoo import models, fields


class OpenAcademyWizard(models.TransientModel):
    _name = 'openacademy.wizard'
    _description = 'Wizard: Quick Registration of Attendees to Sessions'

    def _default_session(self):
        return self.env['openacademy.session'].browse(self._context.get('active_ids'))

    session_ids = fields.Many2many('openacademy.session', string='Sessions', required=True, default=_default_session)
    attendee_ids = fields.Many2many('res.partner', string='Attendees')

    def add_attendees(self):
        for session in self.session_ids:
            session.attendee_ids |= self.attendee_ids
        return {}
