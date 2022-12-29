from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Local app imports
from . import views 
app_name = "tourist"

router = DefaultRouter()

# General Routes
router.register("", views.TouristGeneralViewSet)

# Auth Routes
router.register("update", views.TouristAuthViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
