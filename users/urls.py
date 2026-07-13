from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='cadastro'),
    path('forgot/', views.forgot_view, name='forgot'),
]