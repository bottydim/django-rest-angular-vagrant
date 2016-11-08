"""npss URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^articles/', include('stream.articles.urls', namespace='articles')),
    url(r'^categories/', include('stream.categories.urls', namespace='categories')),
    url(r'^comments/', include('stream.comments.urls', namespace='comments')),
    url(r'^pictures/', include('stream.pictures.urls', namespace='pictures')),
    url(r'^roles/', include('stream.roles.urls', namespace='roles')),
    url(r'^topics/', include('stream.topics.urls', namespace='topics')),
    url(r'^users/', include('stream.users.urls', namespace='users')),
    url(r'^videos/', include('stream.videos.urls', namespace='videos')),
]

admin.autodiscover()
