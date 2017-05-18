from django.conf.urls import url
from . import views

app_name = 'registration'

urlpatterns = [
	url(r'^sign-up/$', views.sign_up, name='sign_up'),
	url(r'^edit-profile/$', views.edit_profile, name='edit_profile'),
]