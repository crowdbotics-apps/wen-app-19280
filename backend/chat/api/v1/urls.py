from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    MessageViewSet,
    ThreadMemberViewSet,
    MessageActionViewSet,
    ThreadActionViewSet,
    ForwardedMessageViewSet,
    ThreadViewSet,
)

router = DefaultRouter()
router.register("threadmember", ThreadMemberViewSet)
router.register("message", MessageViewSet)
router.register("forwardedmessage", ForwardedMessageViewSet)
router.register("threadaction", ThreadActionViewSet)
router.register("messageaction", MessageActionViewSet)
router.register("thread", ThreadViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
