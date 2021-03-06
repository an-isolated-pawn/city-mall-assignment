from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'profile', views.ProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]