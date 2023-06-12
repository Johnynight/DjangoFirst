from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import logout_view

from .views import register

urlpatterns = [
    # path('login/', LoginView.as_view(), name='login'),
    # path('logout/', logout_view, name='logout')
    path('', include('django.contrib.auth.urls')),
    path('register/',register, name='register')
]
