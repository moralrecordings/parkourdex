from django.contrib import admin
from django.contrib.auth import views as auth
from django.urls import path, include
from django.views.generic import TemplateView

from parkourdex.api_v1 import api_v1_router

urlpatterns = [
    path( 'map/', TemplateView.as_view( template_name='trainingmap.html' ) ),
    path( 'api/v1/', include( api_v1_router.urls ) ),
    path( 'admin/', admin.site.urls ),
    path( '', include( 'django_registration.backends.activation.urls' ) ),
    path( 'password_reset/', auth.PasswordResetView.as_view(), name='password_reset' ),
    path( 'password_reset/done/', auth.PasswordResetDoneView.as_view(), name='password_reset_done' ),
    path( 'reset/<uidb64>/<token>/', auth.PasswordResetConfirmView.as_view(), name='password_reset_confirm' ),
    path( 'reset/done/', auth.PasswordResetCompleteView.as_view(), name='password_reset_complete' ),
]
