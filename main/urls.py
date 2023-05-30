from django.urls import path

from .views import home, second_view, base_view

urlpatterns = [
    path('', home, name='home'),
    path('second/', second_view, name='second'),
    path('base/', base_view, name='base'),

]