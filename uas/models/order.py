from odoo import models, fields, api, _
# _ untuk translate

class order(models.Model):
    _name = 'uas.order'
    _description = 'class untuk menyimpan data order'

    nomor = fields.Char('ID Order', size=64, required=True, index=True, readonly=True,
                       states={'draft': [('readonly', False)]})
    name = fields.Char(compute="_compute_name", store=True, recursive=True)
    # semester = fields.Selection([('Genap', 'Genap'),
    #                              ('Gasal', 'Gasal')], 'Semester', required=True, readonly=True,
    #                             default='Genap', states={'draft': [('readonly', False)]}, )
    tahun = fields.Char("Tahun", size=15, default="Gasal - 2022", required=True, readonly=True,
                        states={'draft': [('readonly', False)]})

    customer_id = fields.Many2one('uas.customer', string="Customer", readonly=True, ondelete='cascade', states={'draft': [('readonly', False)]})

    product_id = fields.Many2one('uas.product', string="Product", readonly=True, ondelete='cascade', states={'draft': [('readonly', False)]})
    state = fields.Selection([('draft', 'Draft'),
                              ('done', 'Approved'),
                              ('canceled', 'Canceled')], 'State', required=True, readonly=True,
                             default='draft')
    description = fields.Text('Description', readonly=True, states={'draft': [('readonly', False)]})
    date = fields.Date('Tanggal Pemesanan', default=fields.Date.context_today, readonly=True)
    # mk_id = fields.Many2one('uas.rawmaterial', string='Mata Kuliah', readonly=True, ondelete="cascade",
    #                           states={'draft': [('readonly', False)]},
    #                           domain="[('state', '=', 'confirmed')]")
    shipment_ids = fields.One2many('uas.shipment','order_id', string='Shipmet')
    line_ids = fields.One2many('uas.order.lines', 'kelas_id', string='Nilai', readonly=True,
                                     states={'draft': [('readonly', False)]})
    _sql_constraints = [('name_unik', 'unique(customer_id, semester, tahun)', _('The class is already exist for the sememster!'))]

    @api.depends('customer_id.name','tahun')
    def _compute_name(self):
        for s in self:
            s.name = "%s - %s " % (s.customer_id.name, s.tahun)

    def action_done(self):
        self.state = 'done'

    def action_canceled(self):
        self.state = 'canceled'

    def action_settodraft(self):
        self.state = 'draft'

    def action_wiz_uas(self):
        return {
            'type': 'ir.actions.act_window',
            'name': _('Wizard Total Product'),
            'res_model': 'wiz.uas.order',
            'view_mode': 'form',
            'target': 'new',
            'context': {'active_id': self.id},
        }


class order_lines(models.Model):
    _name = 'uas.order.lines'
    _description = 'class untuk menyimpan data nilai suatu kelas'

    kelas_id = fields.Many2one('uas.order', string='Order', ondelete="cascade")
    mhs_id = fields.Many2one('uas.product', string='Detail Data', ondelete="restrict")
    total = fields.Selection([('1000', '1000'),
                              ('2000', '2000'),
                              ('3000', '3000'),
                              ('4000', '4000'),
                              ('5000', '5000')])
    jumlahh = fields.Char('Jumlah', size=64, required=True, index=True, ondelete="cascade", readonly=False,states={'draft': [('readonly', False)]})
    _sql_constraints = [('name_unik', 'unique(kelas_id, mhs_id)', _('The student is already exist!'))]
