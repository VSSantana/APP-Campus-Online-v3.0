from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
from .views import DashboardView, _PasswordChangeView, _PasswordChangeDoneView


urlpatterns = [
    path('entrar/', LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('sair/', LogoutView.as_view(template_name='campus_app/home.html'), name="logout"),
    path('painel/', DashboardView.as_view(), name='dashboard'),
    path('alterar-senha/', _PasswordChangeView.as_view(), name='edit_password'),
    path('alterar-senha/senha-alterada-com-sucesso', _PasswordChangeDoneView.as_view(), name='password_change_done')
]
