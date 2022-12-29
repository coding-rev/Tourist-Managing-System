"""tms URL Configuration

"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="TMS",
        default_version="v1",
        description="API documentation for TMS",
        terms_of_service="",
        contact=openapi.Contact(email=""),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path(
        "api/v1/docs", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"
    ),
    path("admin/", admin.site.urls),
    path("api/v1/tourists/", include("tourist.urls")),
    path("api/v1/payments/", include("payment.urls")),
]
