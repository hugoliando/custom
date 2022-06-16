{
    'name': 'Manufaktur', #nama modul yg dibaca user di UI
    'version': '1.0',
    'author': 'Hugo',
    'summary': 'Modul UAS SIB UK Petra', #deskripsi singkat dari modul
    'description': 'Ideas management module', #bisa nampilkan gambar/ deskripsi dalam bentuk html. html diletakkan
    #di idea/static/description, bisa kasi icon modul juga.
    'category': 'Latihan',
    'website': 'http://sib.petra.ac.id',
    'depends': ['base', 'sales_team'], # list of dependencies, conditioning startup order
    'data': [ 'views/customer_views.xml',
              'views/order_views.xml',
              'views/product_views.xml',
              'views/rawmaterial_views.xml',
              'views/employee_views.xml',
              'views/shipment_views.xml',
              'security/ir.model.access.csv',
              'wizard/wiz_uas_order_views.xml'],
    'qweb':[], #untuk memberi tahu tempat static file, misal CSS, javascript – html yang lgs dijalnkan (jk ada)
    'demo': [], # demo data (for unit tests)
    'installable': True,
    'auto_install': False, # indikasi install, saat buat database baru
}