"""janus URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
    path('dartboard/admin/', admin.site.urls),
    path('dartboard/', include('dartboard.urls', namespace="dartboard")),
    path('', RedirectView.as_view(url='/personal_homepage/', permanent=False)),
    path('personal_homepage/', include('personal_homepage.urls', namespace="personal_homepage")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('health/', include('health_check.urls')),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
