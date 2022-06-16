from odoo import models, fields, api, _
# _ untuk translate

class employee(models.Model):
    _name = 'uas.employee'
    _description = 'class untuk berlatih tentang employee'
    _rec_name = 'name'
    _order = 'name asc'

    name = fields.Char('Nama Employee', size=64, required=True, index=True, readonly=True,states={'draft': [('readonly', False)]})
    nomor = fields.Char('ID Employee', size=64, required=True, index=True, readonly=True,
                       states={'draft': [('readonly', False)]})
    nohp = fields.Char('No Handphone', required=True, index=True, readonly=True,
                      states={'draft': [('readonly', False)]})
    state = fields.Selection([('draft', 'Draft'),
                              ('confirmed', 'Confirmed'),], 'State', required=True, readonly=True,
                             default='draft')
    email = fields.Char('Email', size=64, required=True, index=True, readonly=True,
                       states={'draft': [('readonly', False)]})
    status = fields.Selection([('aktif', 'Aktif'),
                             ('tidakaktif', 'Tidak Aktif'),], 'Status', required=True, readonly=True, states={'draft': [('readonly', False)]})
    khs_ids = fields.One2many('uas.product', 'name', string='KHS', default=0)
    description = fields.Text('Description', readonly=True, states={'draft': [('readonly', False)]})
    alamat = fields.Char('Alamat', size=64, required=True, index=True, readonly=True,states={'draft': [('readonly', False)]})
    usia = fields.Char('Usia', required=True, index=True, readonly=True,
                       states={'draft': [('readonly', False)]})
    product_ids = fields.One2many('uas.product','employee_id', string='Employee')
    _sql_constraints = [('nomor_unik', 'unique(nomor)', _('ID must be unique!'))]
    # voter_id = fields.Many2one('res.users', 'Voted By', readonly=True, ondelete="cascade", default=lambda self: self.env.user)
    # idea_id = fields.Many2one('idea.idea', string='Idea', readonly=True, ondelete="cascade", states={'draft': [('readonly', False)]},  domain="[('state', '=', 'done'),('active','=','True')]")

    def action_confirmed(self):
        self.state = 'confirmed'

    def action_settodraft(self):
        self.state = 'draft'