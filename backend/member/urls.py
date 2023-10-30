from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signUp, name='signup'),
    path('login/', views.login, name='login'),
    path('reset_password/', views.reset_password, name='reset-password'),
    path('new_password/', views.new_password, name='new-password')
]
