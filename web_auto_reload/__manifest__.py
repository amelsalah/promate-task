
{
   
    'name': ' Auto Refresh',
    'version': '15.0',
    'summary': """
        This module for auto refresh
    """,

    'description': """
        This module essentially provides us a very useful feature to refresh the page in given interval.
        Web Auto Refresh and Reload
		auto refresh web browser
		auto refresh web page
		auto refresh browser web development
		web development auto refresh
		web development auto reload browser
		web auto refresh
		Web Auto Refresh
		Odoo Web Auto Refresh
		Odoo Web Auto Reload
		Web Auto Refresh
		Web Auto Reload
		Auto refresh webpage
		Auto reload webpage
		Automatically reloads web
		Automatically web reload
		Automatically web refresh
		Auto Web Refresh
		Auto Web Reload
		Automatically web refresh and reload
		automatically refresh
		Web Auto
		Auto Web
		Auto Refresh
		Auto Reload
		web refresh
		web reload
		Odoo web
		web odoo
		Refresh
		Reload
		Auto
		Web
    """,
    
    'author': 'Amal Salah',

   
    'depends': ['web'],

    'data': [
        'view/web_auto_refresh_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'web_auto_reload/static/src/js/auto_refresh.js',
        ],
     },

  

    'installable': True,
    'auto_install': False,
}
