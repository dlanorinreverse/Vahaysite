# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def sign_up(request):
	if request.user.is_authenticatd:
		return redirect('/')
	