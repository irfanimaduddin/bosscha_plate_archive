"""bosscha_plate_archive URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import static, include

from plate_archive.views import HomeView

urlpatterns = [
    # path('', HomeView.as_view(), name="home"),
    # path('plate/', include('plate_archive.urls')),
    path('', admin.site.urls),
]

urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = settings.SITE_HEADER # Django administration -> in <h1>
admin.site.site_title = settings.SITE_TITLE # Django site admin -> in <title>
admin.site.index_title = settings.ADMIN_INDEX_TITLE # Site administration -> Home Admin Title