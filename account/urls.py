from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import logout_view


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout')

]
