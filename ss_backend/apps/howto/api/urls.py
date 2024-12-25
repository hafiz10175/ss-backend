
from rest_framework import routers
#
from .views import HowToViewSet
#
app_name = 'howto'
#
router = routers.DefaultRouter()
router.register('notes', HowToViewSet, basename='howto')


urlpatterns = router.urls
