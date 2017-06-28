from django.conf.urls import  url
from . import views

urlpatterns = [
    url(r'^$', views.homepage, name="homepage" ),
url(r'^(?P<id>\d+)/$',views.detail,name="detail"),
url(r'^post/create/$', views.create ,name="create"),
url(r'^(?P<id>\d+)/edit/$', views.update ),

url(r'^(?P<abc>\d+)/delete/$', views.delete,name="delete" ),
]
