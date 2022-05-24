from odoo import models, fields, api

class peminjaman(models.Model):
    _name = 'perpustakaan.peminjaman'
    _description = 'class peminjaman'
    _rec_name = "id_peminjaman"

    id_peminjaman = fields.Char('No.Peminjaman', size=64, readonly=True , required=True, index=True, states={'draft': [('readonly', False)]})
    date = fields.Date('Tanggal Pinjam', default=fields.Date.context_today, readonly=True)
    tanggal_kembali = fields.Date('Tanggal Kembali', default=fields.Date.context_today)
    admin_id = fields.Many2one('res.users','Admin User', readonly=True, ondelete='cascade', default=lambda self: self.env.user)
    anggota_id = fields.Many2one('perpustakaan.anggota', string="Anggota", readonly=True, ondelete='cascade', states={'draft': [('readonly', False)]}, domain="[('state','=','done')]")
    buku_id = fields.Many2one('perpustakaan.buku', string='Buku', readonly=True, ondelete='cascade', states={'draft': [('readonly', False)]}, domain="[('state','=','confirmed')]")
    denda = fields.Integer("Biaya Denda", compute="_compute_denda", store=True, default=0)
    deadline = fields.Date('Deadline', default=fields.Date.context_today, readonly=True,states={'draft': [('readonly', False)]})
    _sql_constraints = [('id_peminjaman_unik', 'unique(id_peminjaman)', ('peminjaman must be unique!'))]

    state = fields.Selection(
        [('draft', 'Draft'),
         ('confirmed', 'Confirmed'),
         ('canceled', 'Canceled')], 'State', required=True, readonly=True, default='draft')

    @api.depends('tanggal_kembali', 'deadline')
    def _compute_denda(self):
        if self.deadline and self.tanggal_kembali:
            deadline = fields.Datetime.from_string(self.deadline)
            tanggal_kembali = fields.Datetime.from_string(self.tanggal_kembali)
            if self.tanggal_kembali > self.deadline:
                self.denda = abs((tanggal_kembali - deadline).days) * (5000)
            if self.tanggal_kembali < self.deadline:
                self.denda = 0


    def action_confirmed(self):
        self.state = 'confirmed'

    def action_canceled(self):
        self.state = 'canceled'

    def action_settodraft(self):
        self.state = 'draft'