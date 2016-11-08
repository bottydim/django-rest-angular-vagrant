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
    url(r'^articles/', include('television.articles.urls', namespace='articles')),
    url(r'^categories/', include('television.categories.urls', namespace='categories')),
    url(r'^comments/', include('television.comments.urls', namespace='comments')),
    url(r'^pictures/', include('television.pictures.urls', namespace='pictures')),
    url(r'^roles/', include('television.roles.urls', namespace='roles')),
    url(r'^topics/', include('television.topics.urls', namespace='topics')),
    url(r'^users/', include('television.users.urls', namespace='users')),
    url(r'^videos/', include('television.videos.urls', namespace='videos')),
]

admin.autodiscover()
