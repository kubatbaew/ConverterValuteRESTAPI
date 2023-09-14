from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

docs = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
    ),
    public=True,
    permission_classes=(permissions.AllowAny, )
)