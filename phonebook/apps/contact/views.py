from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404

from apps.contact.models import Contact

#Index Page
def index(request, template_name="index.html"):
	args = {}
	contact_list = Contact.objects.all().order_by('-id') #List the Conacts
	args['contact_list'] = contact_list
	return TemplateResponse(request, template_name, args)

#Create Form
def create(request, template_name="form.html"):
	args = {}
	if request.method == "POST":
		name 	= request.POST.get('name')
		email 	= request.POST.get('email')
		phone 	= request.POST.get('phone')
		#Create Contact
		contact_create = Contact.objects.create(
				name = name,
				email = email,
				phone = phone,
			)
		return HttpResponseRedirect(reverse('index'))
	return TemplateResponse(request, template_name, args)

#Edit Form
def update(request, contact_id, template_name="form.html"):
	args = {}
	#Get Contact Object with ID
	contact_id = get_object_or_404(Contact, id=contact_id)
	args['contact_id'] = contact_id
	if request.method == "POST":
		name 	= request.POST.get('name')
		email 	= request.POST.get('email')
		phone 	= request.POST.get('phone')

		#Update Contact
		contact_id.name = name
		contact_id.email = email
		contact_id.phone = phone
		contact_id.save()
		return HttpResponseRedirect(reverse('index'))

	return TemplateResponse(request, template_name, args)

#Detail Page
def detail(request, contact_id, template_name="detail.html"):
	args = {}
	#Get Contact Object with ID
	contact_id = get_object_or_404(Contact, id=contact_id)
	args['contact_id'] = contact_id
	return TemplateResponse(request, template_name, args)

#Delete Record
def delete(request, contact_id):
	#Get Contact Object with ID
	contact_id = get_object_or_404(Contact, id=contact_id)
	contact_id.delete()
	return HttpResponseRedirect(reverse('index'))