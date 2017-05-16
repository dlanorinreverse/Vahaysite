# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from vahay.models import Vahay
# Create your views here.


def home(request):
	all_vahay = Vahay.objects.all()
	context={
		'all_vahay': all_vahay
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
			context['error_message'] = 'wrong username or password'
			context['username'] = username
				
	return render(request, 'signin.html', context=context)


def sign_out(request):
	logout(request)
	return redirect('/')
