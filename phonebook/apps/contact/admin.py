from django.contrib import admin

from apps.contact.models import Contact

from apps.contact.actions import export_csv, export_txt, export_xls, export_xlsx

class ContactAdmin(admin.ModelAdmin):
	list_display 	= 	('name', 'email', 'phone',)
	actions 		= 	[export_csv, export_txt, export_xls, export_xlsx]
	
admin.site.register(Contact, ContactAdmin)