from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('marketplace.urls')),
    url(r'^api-token-auth/', views.obtain_auth_token)
]
