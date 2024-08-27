from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FlowerViewset,CategoryViewset,ColorViewset,ReviewViewset

router = DefaultRouter()

router.register('list', FlowerViewset,)
router.register('category', CategoryViewset,)
router.register('color', ColorViewset,)
router.register('review', ReviewViewset,)

urlpatterns = [
    path('', include(router.urls)),
]