from django.urls import path, include
from rest_framework.routers import SimpleRouter
from board_app import views

router = SimpleRouter()
router.register("posts", views.BoardFlowPostViewSet)

urlpatterns = [
    path("", include(router.urls))
]