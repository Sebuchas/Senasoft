
from django.urls import include, path
from django.contrib import admin
from main.views import index, inicio, certificado
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

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
from main.views import inicio
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
# from main.views import SignUpView, BienvenidaView,SignInView, SignOutView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/', include('Usuario.urls')),
    path('sondeo/', include('Sondeo.urls')),
<<<<<<< HEAD
    path('', inicio, name="inicio"),
=======

    path('', index , name="index"),
    path('', inicio , name="inicio"),
    path('certificado/', certificado , name="certificado"),
    
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='usuario-login'),
    path('logout/', auth_views.LogoutView.as_view(), name='usuario-logout'),
    path('registrar/',include('cuenta.urls')),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html',email_template_name='registration/password_reset_email.html'),
         name='password_reset'),
    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),


    # path('', inicio , name="inicio"),
>>>>>>> 65d29efbc3ffabd19efcb5c989ad459e0793908f
    # path('certificado/', certificado , name="certificado"),
    #  # Logueo
    # path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='usuario-login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='usuario-logout'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


