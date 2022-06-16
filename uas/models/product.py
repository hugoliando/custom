from odoo import models, fields, api, _
# _ untuk translate

class product(models.Model):
    _name = 'uas.product'
    _description = 'class untuk berlatih tentang product'
    _order = 'name asc'

    name = fields.Char('Nama Product', size=64, required=True, index=True, readonly=True,states={'draft': [('readonly', False)]})
    price = fields.Integer('Harga (Rp.)', required=True, index=True, readonly=True,
                      states={'draft': [('readonly', False)]})
    state = fields.Selection([('draft', 'Draft'),
                              ('confirmed', 'Confirmed'),], 'State', required=True, readonly=True,
                             default='draft')
    # status = fields.Selection([('aktif', 'Aktif'),
    #                          ('tidakaktif', 'Tidak Aktif'),], 'Status', required=True, readonly=True, states={'draft': [('readonly', False)]})
    description = fields.Text('Description', readonly=True, states={'draft': [('readonly', False)]})
    customer_id = fields.Many2one('uas.customer', string="Customer", readonly=True, ondelete='cascade', states={'draft': [('readonly', False)]})
    employee_id = fields.Many2one('uas.employee', string="Employee", readonly=True, ondelete='cascade', states={'draft': [('readonly', False)]})
    shipment_ids = fields.One2many('uas.shipment','product_id', string='Product')
    # line_ids = fields.One2many('uas.productline', 'detail_id', string='line')
    detail_ids = fields.One2many('uas.product.lines','product_id', string='detail',readonly=True,
                                    states={'draft': [('readonly', False)]})
    product_ids = fields.One2many('uas.order','product_id', string='Product')
    # rawmaterial_id = fields.Many2one('uas.rawmaterial', string="Raw Material", readonly=True, ondelete='cascade', states={'draft': [('readonly', False)]})
    # voter_id = fields.Many2one('res.users', 'Voted By', readonly=True, ondelete="cascade", default=lambda self: self.env.user)
    # idea_id = fields.Many2one('idea.idea', string='Idea', readonly=True, ondelete="cascade", states={'draft': [('readonly', False)]},  domain="[('state', '=', 'done'),('active','=','True')]")

    def action_confirmed(self):
        self.state = 'confirmed'

    def action_settodraft(self):
        self.state = 'draft'

class product_lines(models.Model):
    _name = 'uas.product.lines'
    _description = 'class untuk berlatih tentang productline'

    product_id = fields.Many2one('uas.product', string='product', ondelete="cascade")
    rawmaterial_id = fields.Many2one('uas.rawmaterial', string='Detail Data', ondelete="restrict")
    jumlah = fields.Selection([('1000', '1000'),
                              ('2000', '2000'),
                              ('3000', '3000'),
                              ('4000', '4000'),
                              ('5000', '5000')])
    jumlahh = fields.Char('Jumlah', size=64, required=True, index=True, ondelete="cascade", readonly=False,states={'draft': [('readonly', False)]})

    _sql_constraints = [('name_unik', 'unique(product_id, rawmaterial_id)', _('The student is already exist!'))]