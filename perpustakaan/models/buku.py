from odoo import models, fields, api

class buku(models.Model):
    _name = 'perpustakaan.buku'
    _description = 'class buku'
    _rec_name = "judul"

    id_buku = fields.Char('ID Buku', size=8, readonly=True , required=True, index=True, states={'draft': [('readonly', False)]})
    judul = fields.Char('Judul Buku', size=64, readonly=True , required=True, index=True, states={'draft': [('readonly', False)]})
    pengarang = fields.Char('Pengarang', size=64, readonly=True ,required=True, index=True, states={'draft': [('readonly', False)]})
    penerbit = fields.Char('Penerbit', size=64, readonly=True , required=True, index=True, states={'draft': [('readonly', False)]})
    _sql_constraints = [('id_buku_unik', 'unique(id_buku)', ('buku must be unique!'))]

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

    def test_buku(self):
        print("test buku")
        t = self.env.context
        print(t.get("keterangan"))