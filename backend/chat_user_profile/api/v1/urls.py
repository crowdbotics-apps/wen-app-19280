from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ContactViewSet, ProfileViewSet, VerificationCodeViewSet

router = DefaultRouter()
router.register("verificationcode", VerificationCodeViewSet)
router.register("contact", ContactViewSet)
router.register("profile", ProfileViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
