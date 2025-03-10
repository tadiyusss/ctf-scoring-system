"""
URL configuration for ctf_scoring project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from ctf_scoring import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("vbacVFk4UiW73slQaH/", admin.site.urls),
    path("", views.user_login, name = "login"),
    path("register/", views.register, name = "register"),
    path("dashboard/", views.dashboard, name = "dashboard"),
    path("flags/", views.flags, name = "flags"),
    path("leaderboard/", views.leaderboard, name = "leaderboard"),
    path("leaderboard_data/", views.leaderboard_data, name = "leaderboard_data"),
    path("logout/", views.logout_user, name = "logout"),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
