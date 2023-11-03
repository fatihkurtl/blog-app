from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signUp, name='signup'),
    path('login/', views.login, name='login'),
    path('update/<str:username>/<int:pk>/', views.profile_update, name='update_profile'),
    path('delete/<str:username>/<int:pk>/', views.delete_member, name='delete-member'),
    path('set_password/<str:username>/<int:pk>/', views.set_password, name='set_password'),
    path('reset_password/', views.reset_password, name='reset-password'),
    path('new_password/', views.new_password, name='new-password')
]
