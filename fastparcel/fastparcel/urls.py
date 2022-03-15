"""fastparcel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from core import views
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
#from django.views.generic import TemplateView

from core.customer import views as customer_views
from core.courier import views as courier_views

customer_urlpatters = [
    path('', customer_views.home, name='home'),
    path('profile/', customer_views.profile_page, name="profile"),
]

courier_urlpatters = [
    path('', courier_views.home, name='home')
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),

    path('sign-in/', auth_views.LoginView.as_view(template_name='sign_in.html')),
    path('sign-out/', auth_views.LogoutView.as_view(next_page='/')),
    path('sign-up/',views.sign_up),

    path('customer/', include((customer_urlpatters,'customer'))),
    path('courier/', include((customer_urlpatters,'courier'))),
]
