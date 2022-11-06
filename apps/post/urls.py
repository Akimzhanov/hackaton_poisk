from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    LostViewSet
)

router = DefaultRouter()
router.register('lost', LostViewSet, 'lost')

urlpatterns = [

]

urlpatterns += router.urls
