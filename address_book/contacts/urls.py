from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^login/$', views.login_user, name='login'),
    url(r'^singup/$', views.singup, name='singup'),
    url(r'^show/$', views.show_contacts, name='show_contacts'),
    url(r'^new/$', views.new_contact, name='new_contact'),
    url(r'^edit/(?P<id_contact>\d{1,})/$', views.edit_contact, name='edit_contact'),
    url(r'^delete/(?P<id_contact>\d{1,})/$', views.delete_contact, name='delete_contact'),

]
