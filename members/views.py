from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members

import datetime

def index(request):
	mymembers = Members.objects.all().order_by('firstname').values()
	# template = loader.get_template('index.html')

	context = {
		'members': mymembers
	}

	# return HttpResponse(template.render(context, request))
	return render(request, 'index.html', context)

def add(request):
	template = loader.get_template('add.html')

	return HttpResponse(template.render({}, request))

def addmember(request):
	x = request.POST['first']
	y = request.POST['last']
	Members(firstname=x, lastname=y).save()

	return HttpResponseRedirect(reverse('test'))

def delete(request, id):
	Members.objects.get(id=id).delete()

	return HttpResponseRedirect(reverse('test'))

def update(request, id):
	member = Members.objects.get(id=id)
	template = loader.get_template('update.html')

	context = {
		'member': member
	}

	return HttpResponse(template.render(context, request))

def updatemember(request, id):
	member = Members.objects.get(id=id)
	member.firstname = request.POST['first']	
	member.lastname = request.POST['last']
	member.save()

	return HttpResponseRedirect(reverse('test'))

