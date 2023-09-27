
from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register(r"blog-post",BlogPostViews)
router.register(r"tags",TagViews)
router.register(r"categories",CategoryView)
router.register(r"comments",CommentViews)



urlpatterns = [
    path("",include(router.urls)),
]
