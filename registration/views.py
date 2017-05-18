# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import authenticate, login

# Create your views here.

def sign_up(request):
	if request.user.is_authenticated:
		return redirect('/')

	context={}

	if request.method == "POST":
		username = request.POST.get('username')
		f_name = request.POST.get('first_name')
		l_name = request.POST.get('last_name')
		email = request.POST.get('email')
		password = request.POST.get('password')
		r_password = request.POST.get('re_enter_password')
		user = User.objects.filter(username=username)
		
		context['username'] = username
		context['f_name'] = f_name
		context['l_name'] = l_name
		context['email'] = email

		if user:
			context['username_error'] = "Username already taken!"
			return render(request, 'registration/signup.html', context=context)

		if not password == r_password:
			context['pass_error'] = "Password do not match"
			return render(request, 'registration/signup.html', context=context)

		User.objects.create_user(username=username, email=email, first_name=f_name, last_name=l_name, password=password)
		user = authenticate(username=username, password=password)
		if user:
			login(request,user)
			return redirect(reverse('profile', kwargs={'username': username}))

	return render(request, 'registration/signup.html', context=context)


def edit_profile(request):
	if not request.user.is_authenticated:
		return redirect('/')

	if request.method == "POST":
		request.user.first_name = request.POST.get('first_name')
		request.user.last_name = request.POST.get('last_name')
		request.user.email = request.POST.get('email')
		request.user.save()
		return redirect(reverse('profile', kwargs={'username': request.user.username}))

	return render(request, 'registration/edit_profile.html')







