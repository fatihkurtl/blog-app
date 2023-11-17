from django.urls import path

from . import views

urlpatterns = [
    path('', views.EmailSubscribeViewSet.as_view(), name='email-subscribe'),
]
