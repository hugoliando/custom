from odoo import models, fields, api, _

class wizorder(models.TransientModel):
    _name = 'wiz.uas.order'
    _description = 'class untuk menyimpan data kelas dan nilai'

    kelas_id = fields.Many2one('uas.order', String='Kelas')

    # semester = fields.Selection(related='kelas_id.semester')
    tahun = fields.Char(related='kelas_id.tahun')

    customer_id = fields.Many2one(related='kelas_id.customer_id')

    line_ids = fields.One2many('wiz.uas.order.lines', 'wiz_header_id', string='Customer')

    def action_confirmed(self):
        self.state = 'done'

    def action_canceled(self):
        self.state = 'canceled'

    def action_settodraft(self):
        self.state = 'draft'

    def action_confirm(self):
        for rec in self.line_ids:
            rec.ref_kelas_lines_id.jumlahh = rec.jumlahh

    @api.model
    def default_get(self,fields_list):  # ini adalah common method, semacam constructor, akan dijalankan saat create object. Ini akan meng-overwrite default_get dari parent
        res = super(wizorder, self).default_get(fields_list)
        # res  merupakan dictionary beserta value yang akan diisi, yang sudah diproses di super class (untuk create record baru)
        res['kelas_id'] = self.env.context['active_id']
        return res

    @api.onchange('kelas_id')
    def onchange_kelas_id(self):
        if not self.kelas_id:
            return
        vals = []
        line_ids = self.env['wiz.uas.order.lines']
        for rec in self.kelas_id.line_ids:
            line_ids += self.env['wiz.uas.order.lines'].new({
                'wiz_header_id': self.id,
                'mhs_id': rec.mhs_id.id,
                'ref_kelas_lines_id': rec.id
            })
            # cara membuat record baru di m2m atau o2m
        self.line_ids = line_ids


class order_lines_wiz(models.TransientModel):
    _name = 'wiz.uas.order.lines'
    _description = 'class untuk menyimpan data nilai suatu kelas'

    wiz_header_id = fields.Many2one('wiz.uas.order', string='Kelas')
    mhs_id = fields.Many2one('uas.product', string='Products', ondelete="restrict")
    ref_kelas_lines_id = fields.Many2one('uas.order.lines')
    total = fields.Selection([('1000', '1000'),
                              ('2000', '2000'),
                              ('3000', '3000'),
                              ('4000', '4000'),
                              ('5000', '5000')])
    jumlahh = fields.Char('Jumlah', size=64, required=True, index=True, ondelete="cascade", readonly=False,states={'draft': [('readonly', False)]})

