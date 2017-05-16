# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Vahay
# Create your views here.

def vahay_details(request, pk):
	if not request.user.is_authenticated:
		return redirect('/')

	vahay = get_object_or_404(Vahay, pk=pk)
	return render(request, 'vahay/vahayDetails.html', {'vahay': vahay})


def add_vahay(request, username):
	if not request.user.is_authenticated:
		return redirect('/')
	
	if request.method == "POST":
		name = request.POST.get('name')
		rent_range = request.POST.get('rent_range')
		category = request.POST.get('category')
		contact_details = request.POST.get('contacts')
		location = request.POST.get('location')
		Vahay.objects.create(owner=request.user, name=name, rent_range=rent_range, category=category,
		 contact_details=contact_details, location=location)
		return redirect(reverse('profile', kwargs={'username': request.user.username}))

	return render(request, 'vahay/addVahay.html')			