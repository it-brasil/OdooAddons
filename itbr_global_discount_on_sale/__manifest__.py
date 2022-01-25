# -*- coding: utf-8 -*-
#############################################################################
#
#    MMF Serviços de Tecnologia da Informação
#
#    Copyright (C) 2021-TODAY IT Brasil(<https://www.itbrasil.com.br>)
#    Author: IT Brasil(<https://www.itbrasil.com.br>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
{
    'name': "Global Discount on Sale Order",
    'summary': """Customisation to provide global discount on Sale Order.""",
    'description': """Customisation to provide global discount on Sale Order. The global discount will be affected on invoice and related journal.""",
    'category': "Sales",
    'version': "14.0.1.0.0",
    'author': "IT Brasil",
    'company': "IT Brasil",
    'maintainer': "IT Brasil",
    'website': "www.itbrasil.com.br",
    'depends': ['sale_management', 'account'],
    'data': [
        'report/sale_report_templates.xml',
        'security/security.xml',
        'views/account_move_views.xml',
        'views/report_invoice.xml',
        'views/res_config_settings_views.xml',
        'views/sale_order_views.xml',
        'views/sale_portal_templates.xml',
    ],
    'images': [
        'static/description/banner.jpg',
    ],
    'license': "LGPL-3",
    'installable': True,
    'application': False,
    'auto_install': False,
}
