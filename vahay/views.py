# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect

from .models import Vahay
# Create your views here.

def vahay_details(request, pk):
	vahay = get_object_or_404(Vahay, pk=pk)
	return render(request, 'vahay/vahayDetails.html', {'vahay': vahay})


def add_vahay(request, username):
	if not request.user.is_authenticated:
		return redirect('/')
	
	return render(request, 'vahay/addVahay.html')			