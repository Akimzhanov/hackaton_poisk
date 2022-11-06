from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import FindViewSet


router = DefaultRouter()
router.register('find', FindViewSet, 'find')

urlpatterns = [

]

urlpatterns += router.urls




