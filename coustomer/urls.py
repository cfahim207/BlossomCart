from django.urls import path, include
from rest_framework.routers import DefaultRouter
from coustomer import views

router = DefaultRouter()

router.register('list', views.CoustomerViewset,)
router.register('deposite', views.DepositeViewset,)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.UserRegistrationView.as_view(),name='register'),
    path('login/', views.UserLoginApiView.as_view(),name='login'),
    path('logout/', views.UserlogoutView.as_view(),name='logout'),
    path('active/<uid64>/<token>', views.activate,name='activate'),
    path('dashboard/',views.DashboardView.as_view(), name='dashboard')
]