from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from bookapp.views import BookViewSet, UserViewSet


router = routers.DefaultRouter()
router.register(r'book', BookViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
