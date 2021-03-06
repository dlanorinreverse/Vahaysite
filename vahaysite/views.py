# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.http import HttpResponse

from vahay.models import Vahay, WorldBorder

# Create your views here.

def world_data(request):
	world = serialize('geojson', WorldBorder.objects.all())
	return HttpResponse(world, content_type='json')


def vahay_data(request):
	vahay = serialize('geojson', Vahay.objects.all())
	return HttpResponse(vahay, content_type='json')


def home(request):
	all_vahay = Vahay.objects.all()
	context = {
		"all_vahay": all_vahay
	}

	if request.user.is_authenticated:
		return render(request, 'homepage.html', context=context)

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user:
			login(request, user)
			return render(request, 'homepage.html', context=context)
		else:
			context['error_message'] = 'Invalid username or password'
			context['username'] = username
				
	return render(request, 'signin.html', context=context)


def profile(request, username):
	if not request.user.is_authenticated:
		return redirect('/')

	vahays =  request.user.vahay_set.all()
	context = {
		'vahays':vahays
	}
	return render(request, 'profile.html', context=context)


def sign_out(request):
	logout(request)
	return redirect('/')
