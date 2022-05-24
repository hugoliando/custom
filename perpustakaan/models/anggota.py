from odoo import models, fields, api

class anggota(models.Model):
    _name = 'perpustakaan.anggota'
    _description = 'class anggota untuk UTS'
    _rec_name = 'name'

    id_anggota = fields.Char('ID Anggota', size=8, required=True, index=True, readonly=False)
    name = fields.Char('Nama Anggota', size=64, required=True, index=True)
    description = fields.Text('Deskripsi', readonly=True, states={'draft': [('readonly', False)]})
    active = fields.Boolean('Aktif', default=True, readonly=True, states={'draft': [('readonly', False)]})
    _sql_constraints = [('id_anggota_unik', 'unique(id_anggota)', ('anggota must be unique!'))]

    state = fields.Selection(
        [('draft', 'Draft'),
         ('confirmed', 'Confirmed'),
         ('done', 'Done'),
         ('canceled', 'Canceled')], 'State', required=True, readonly=True, default='draft')

    def action_done(self):
        self.state = 'done'

    def action_canceled(self):
        self.state = 'canceled'

    def action_confirmed(self):
        self.state = 'confirmed'

    def action_settodraft(self):
        self.state = 'draft'