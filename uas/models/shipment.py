from odoo import models, fields, api, _
# _ untuk translate

class shipment(models.Model):
    _name = 'uas.shipment'
    _description = 'class untuk berlatih tentang shipment'
    _order = 'name asc'

    name = fields.Char('Shipment Vendor', size=64, required=True, index=True, readonly=True,states={'draft': [('readonly', False)]})
    price = fields.Integer('Biaya (Rp.)', required=True, index=True, readonly=True,
                      states={'draft': [('readonly', False)]})
    state = fields.Selection([('draft', 'Draft'),
                              ('confirmed', 'Confirmed'),], 'State', required=True, readonly=True,
                             default='draft')
    # status = fields.Selection([('aktif', 'Aktif'),
    #                          ('tidakaktif', 'Tidak Aktif'),], 'Status', required=True, readonly=True, states={'draft': [('readonly', False)]})
    description = fields.Text('Description', readonly=True, states={'draft': [('readonly', False)]})
    date = fields.Date('Tanggal Pengiriman', default=fields.Date.context_today, readonly=True)
    customer_id = fields.Many2one('uas.customer', string="Customer", readonly=True, ondelete='cascade', states={'draft': [('readonly', False)]})
    product_id = fields.Many2one('uas.product', string="Product", readonly=True, ondelete='cascade', states={'draft': [('readonly', False)]})
    order_id = fields.Many2one('uas.order', string="Customer", readonly=True, ondelete='cascade', states={'draft': [('readonly', False)]})
    # voter_id = fields.Many2one('res.users', 'Voted By', readonly=True, ondelete="cascade", default=lambda self: self.env.user)
    # idea_id = fields.Many2one('idea.idea', string='Idea', readonly=True, ondelete="cascade", states={'draft': [('readonly', False)]},  domain="[('state', '=', 'done'),('active','=','True')]")

    def action_confirmed(self):
        self.state = 'confirmed'

    def action_settodraft(self):
        self.state = 'draft'