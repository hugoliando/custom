from odoo import models, fields, api, _
# _ untuk translate

class rawmaterial(models.Model):
    _name = 'uas.rawmaterial'
    _description = 'class untuk berlatih tentang rawmaterial'
    _rec_name = 'name'
    _order = 'name asc'

    name = fields.Char('Nama Raw Material', size=64, required=True, index=True, readonly=True,ondelete='cascade',states={'draft': [('readonly', False)]})
    nomor = fields.Char('ID Raw Material', size=64, required=True, index=True, readonly=True,ondelete='cascade',states={'draft': [('readonly', False)]})
    vendor = fields.Char('Vendor', size=64, required=True, index=True, readonly=True,
                       states={'draft': [('readonly', False)]})
    jumlah = fields.Integer('Jumlah', size=64, required=True, index=True, readonly=True,states={'draft': [('readonly', False)]})
    state = fields.Selection([('draft', 'Draft'),
                              ('confirmed', 'Confirmed'),], 'State', required=True, readonly=True,
                             default='draft')
    description = fields.Text('Description', readonly=True, states={'draft': [('readonly', False)]})
    tanggal_masuk = fields.Date('Tanggal Masuk', default=fields.Date.context_today)
    harga = fields.Integer('Harga (pcs)', size=64, required=True, index=True, readonly=True,states={'draft': [('readonly', False)]})
    # detail_id = fields.Many2one('uas.product', string="Detail Data", readonly=True, ondelete='cascade')
    # status = fields.Selection([('aktif', 'Aktif'),
    #                          ('tidakaktif', 'Tidak Aktif'),], 'Status', required=True, readonly=True, states={'draft': [('readonly', False)]})

    # voter_id = fields.Many2one('res.users', 'Voted By', readonly=True, ondelete="cascade", default=lambda self: self.env.user)
    # idea_id = fields.Many2one('idea.idea', string='Idea', readonly=True, ondelete="cascade", states={'draft': [('readonly', False)]},  domain="[('state', '=', 'done'),('active','=','True')]")
    # totalbiaya = fields.Float('Total biaya', size=64, readonly=True, required=False, index=True)
    totalbiayafix = fields.Float(string='Total Biaya', compute='_computeVar', required=False)

    # @api.onchange('harga')
    # def _func_onchange_harga(self):
    #     for test in self:
    #         if test.harga:
    #             a = float(test.jumlah)
    #             b = float(test.harga)
    #             test.totalbiaya = a * b
    #             test.totalbiayafix = float(test.totalbiaya)
    @api.onchange('harga', 'jumlah')
    def _computeVar(self):
        for record in self:
            record.totalbiayafix = record.harga * record.jumlah

    def action_confirmed(self):
        self.state = 'confirmed'

    def action_settodraft(self):
        self.state = 'draft'