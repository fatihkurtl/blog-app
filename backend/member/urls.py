from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signUp, name='signup'),
    path('login/', views.login, name='login'),
    path('update/<str:username>/<int:pk>/', views.ProfileUpdateViewSet.as_view(), name='update_profile'),    
    path('delete/<str:username>/<int:pk>/', views.DeleteMemberViewSet.as_view(), name='delete-member'),
    path('set_password/<str:username>/<int:pk>/', views.SetPasswordViewSet.as_view(), name='set_password'),
    path('reset_password/', views.ResetPasswordViewSet.as_view(), name='reset-password'),
    path('new_password/', views.NewPasswordViewSet.as_view(), name='new-password')
]
