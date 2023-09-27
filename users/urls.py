from django.urls import path,include
from .views import UserProfileView ,UserView
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r"userprofile",UserProfileView)
router.register(r"users",UserView)

urlpatterns = [
    path("",include(router.urls)),
]
