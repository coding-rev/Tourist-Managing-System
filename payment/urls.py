from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Local app imports
from . import views 

app_name = "payment"

router = DefaultRouter()

# Routes
router.register("", views.PaymentAuthViewSet)
router.register("sites", views.SiteViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("report/", views.TouristPaymentReportView.as_view()),
    path("zoo/", views.ZooPaymentsView.as_view()),
    path('tourists/no-payment/', views.NoSitePaymentsView.as_view())
]
