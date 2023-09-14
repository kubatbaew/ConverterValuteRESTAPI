from django.contrib import admin
from django.urls import path, include
from core.docs import docs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('converter/', include('apps.converter.urls')),
    path('docs/', docs.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
