from django.db import models

class Contact(models.Model):
	name 	= 	models.CharField(verbose_name="Name", max_length=128, blank=True, null=True)
	email 	= 	models.EmailField(verbose_name="Email", max_length=128, blank=True, null=True)
	phone 	= 	models.CharField(verbose_name="Phone Number", max_length=128, blank=True, null=True)

	def __unicode__(self):
		return self.name
