# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.gis.geos import Point

from .models import Vahay
from .models import Review
from .models import Image
# Create your views here.


def search_vahay(request):
	if not request.user.is_authenticated:
		return redirect('/')

	if request.method == "POST":
		result = []
		address = request.POST.get('search')
		vahays = Vahay.objects.all()
		for vahay in vahays:
			if str(address).upper() in str(vahay.address).upper():
				result.append(vahay)
		context = {
			'result': result,
			'address': address
		}
		return render(request, 'vahay/searchResults.html', context=context)

	return redirect('/')

def vahay_details(request, pk):
	if not request.user.is_authenticated:
		return redirect('/')

	vahay = get_object_or_404(Vahay, pk=pk)
	reviews = Review.objects.filter(vahay=vahay).order_by('-when_created')
	images = Image.objects.filter(vahay=vahay)
	context={
		'vahay': vahay,
		'reviews': reviews,
		'images': images
	}
	return render(request, 'vahay/vahayDetails.html', context=context)


def add_vahay(request, username):
	if not request.user.is_authenticated:
		return redirect('/')
	
	if request.method == "POST":
		name = request.POST.get('name')
		rent_range = request.POST.get('rent_range')
		category = request.POST.get('category')
		contact_details = request.POST.get('contacts')
		address = request.POST.get('address')
		details = request.POST.get('details')
		location = Point(123.9014053338178, 10.31127060214643)
		Vahay.objects.create(owner=request.user, name=name, rent_range=rent_range, category=category,
		 contact_details=contact_details, address=address, description=details, location=location)
		return redirect(reverse('profile', kwargs={'username': request.user.username}))

	return render(request, 'vahay/addVahay.html')


def delete_vahay(request, pk):
	vahay = get_object_or_404(Vahay, pk=pk)
	vahay.delete()

	return redirect(reverse('profile', kwargs={'username': request.user.username}))


def add_comment(request, pk):
	if not request.user.is_authenticated:
		return redirect('/')

	redirect_url = request.GET.get('next')

	if request.method == "POST":
		vahay = get_object_or_404(Vahay, pk=pk)
		content = request.POST.get('content')
		Review.objects.create(user=request.user, vahay=vahay, content=content)
		
	return redirect(redirect_url)


def edit_vahay(request, pk):
	if not request.user.is_authenticated:
		return redirect('/')

	vahay = get_object_or_404(Vahay, pk=pk)
	context = {
		'vahay': vahay
	}

	if request.method == "POST":
		vahay.name = request.POST.get('vahay_name')
		vahay.rent_range = request.POST.get('rent_range')
		vahay.category = request.POST.get('category')
		vahay.contact_details = request.POST.get('contacts')
		vahay.address = request.POST.get('address')
		vahay.description = request.POST.get('description')
		if request.POST.get('available', None) == None:
			vahay.available = 0
		else:
			vahay.available = 1

		vahay.save()
		if request.POST['image_link']:
			image_link = request.POST.get('image_link')
			Image.objects.create(vahay=vahay, link=image_link)
		return redirect(reverse('profile', kwargs={'username': request.user.username}))

	return render(request, 'vahay/editVahay.html', context=context)


def vote_vahay(request, pk):
	if not request.user.is_authenticated:
		return redirect('/')

	redirect_url = request.GET.get('next')

	if request.method == "POST":
		vahay = get_object_or_404(Vahay, pk=pk)
		vahay.vote += 1
		vahay.save()
		return redirect(redirect_url)

	return redirect('/')




