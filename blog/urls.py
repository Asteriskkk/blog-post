"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include,url
from django.contrib import admin
from accounts.views import Login_View,Logout_View,Register_View
urlpatterns = [
    url(r'^api/', include('api1.urls', namespace="post_api")),
    url(r'^api/comment/', include('comment.comment_api.urls', namespace="post_api")),
    url(r'^admin/', admin.site.urls),
    url(r'^login/',Login_View,name="login"),
    url(r'^logout/',Logout_View,name="logout"),
    url(r'^register/', Register_View, name="register"),
    url(r'^', include('post.urls', namespace="post")),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






