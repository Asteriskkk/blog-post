from django.conf.urls import  url

from .views import CommentView

urlpatterns = [
    url(r'^$',CommentView.as_view(), name="comment_api"),
#  url(r'^(?P<pk>\d+)/$',DetailView.as_view(),name="detail"),
# # url(r'^post/create/$', views.create ,name="create"),
#    url(r'^(?P<pk>\d+)/edit/$',UpdateView.as_view()),
#
#    url(r'^(?P<pk>\d+)/delete/$',DeleteView.as_view(),name="delete" ),
]

