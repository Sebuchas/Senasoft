
# main URL Configuration
# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/4.1/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

from operator import index
from django.urls import include, path
from django.contrib import admin

from main.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
# from main.views import SignUpView, BienvenidaView,SignInView, SignOutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/', include('Usuario.urls')),
    path('sondeo/', include('Sondeo.urls')),
    path('registrar/', include('cuenta.urls')),

    path('', index , name="index"),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='usuario-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='usuario-logout'),

    # path('certificado/', certificado , name="certificado"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)