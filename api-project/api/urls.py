from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_view, name='add'),
    path('subtract/', views.subtract_view, name='subtract'),
    path('multiply/', views.multiply_view, name='multiply'),
    path('divide/', views.divide_view, name='divide'),
]