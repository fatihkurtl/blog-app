"""
URL configuration for src project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from contact.urls import urlpatterns as contact_urlpatterns
from blog.urls import urlpatterns as blog_urlpatterns
from member.urls import urlpatterns as member_urlpatterns
from subscribe_emails.urls import urlpatterns as subscribe_urlpatterns

from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    # path("i18n/", include("django.conf.urls.i18n")),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include([
            path('api/blog/', include(blog_urlpatterns)),
            path('api/contact/', include(contact_urlpatterns)),
            path('api/member/', include(member_urlpatterns)),
            path('api/email_subscribe/', include(subscribe_urlpatterns)),
        ])),
]
# urlpatterns += i18n_patterns(path("admin/", admin.site.urls))

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   