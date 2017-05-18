from django.conf.urls import url
from . import views

app_name = 'vahay'

urlpatterns = [
	url(r'^vahay-details/(?P<pk>\d+)/$', views.vahay_details, name='vahay_details'),
	url(r'^(?P<username>[\w\-]+)/add-vahay/$', views.add_vahay, name='add_vahay'),
	url(r'^vahay-details/(?P<pk>\d+)/add_comment$', views.add_comment, name='add_comment'),
	# url(r'^edit-vahay/$', views.edit_vahay, name='edit_vahay'),
]