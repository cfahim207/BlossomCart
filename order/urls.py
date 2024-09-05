from django.urls import path, include
from rest_framework.routers import DefaultRouter
from order import views

router = DefaultRouter()

router.register('list', views.OrderViewset,)

urlpatterns = [
    path('', include(router.urls)),
]  