from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('entrar/', LoginView.as_view(template_name='accounts/login.html'), name="login")
]
