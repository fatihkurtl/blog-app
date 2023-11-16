from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostViewSet.as_view(), name='posts-list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/<str:category>/', views.PostViewSet.as_view(), name='posts-category'),
    path('post/<str:category>/<int:pk>/', views.PostDetailView.as_view(), name='posts-category'),
    path('post/<int:pk>/comment/', views.PostDetailView.as_view(), name='create-comment'),
]
