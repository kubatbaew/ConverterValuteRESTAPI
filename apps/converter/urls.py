from rest_framework.routers import DefaultRouter

from apps.converter.views import ConverterAPIViewSet

router = DefaultRouter()
router.register('', ConverterAPIViewSet)

urlpatterns = router.urls
