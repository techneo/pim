from django.conf.urls import url

from apps.contact import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'create/$', views.create, name="create"),
    url(r'update/(?P<contact_id>\d+)/$', views.update, name="update"),
    url(r'detail/(?P<contact_id>\d+)/$', views.detail, name="detail"),
    url(r'delete/(?P<contact_id>\d+)/$', views.delete, name="delete"),
]
