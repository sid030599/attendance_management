from rest_framework.routers import DefaultRouter
from .views import ShiftViewSet, WeeklyOffViewSet

router = DefaultRouter()
router.register('shifts', ShiftViewSet)
router.register('weekly-offs', WeeklyOffViewSet)

urlpatterns = router.urls
