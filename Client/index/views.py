# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
	return render(request, 'index/index.html')

def index1(request):
    	return render(request, 'index/index1.html')

def well(request):
    	return render(request, 'index/well.html')

def farms(request):
    	return render(request, 'index/farms.html')

def household(request):
    	return render(request, 'index/household.html')

def landlord(request):
    	return render(request, 'index/landlord.html')

def home(request):
    	return render(request, 'index/home.html')

#def index1(request):
#	template = loader.get_template("index/index1.html")
#	return HttpResponse(template.render())
