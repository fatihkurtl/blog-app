from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.allPosts, name='posts-list'),
    path('post/<int:pk>/', views.postDetail, name='post-detail'),
    path('posts/<str:category>/', views.categorizePosts, name='posts-category'),
    path('post/<str:category>/<int:pk>/', views.categorizeDetail, name='posts-category'),
    path('post/<int:pk>/comment/', views.createComment, name='create-comment'),
]
