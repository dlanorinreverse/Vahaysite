from django.conf.urls import url
from . import views

app_name = 'vahay'

urlpatterns = [
	url(r'^vahay-details/(?P<pk>\d+)/$', views.vahay_details, name='vahay_details'),
	url(r'^(?P<username>[\w\-]+)/add-vahay/$', views.add_vahay, name='add_vahay'),
	url(r'^vahay-details/(?P<pk>\d+)/add_comment$', views.add_comment, name='add_comment'),
	url(r'^(?P<pk>\d+)/edit-vahay/$', views.edit_vahay, name='edit_vahay'),
	url(r'^(?P<pk>\d+)/vote-vahay/$', views.vote_vahay, name='vote_vahay'),
]