from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .apps import LibraryConfig
from . import views

app_name = LibraryConfig.name

router = DefaultRouter()
router.register('books', views.BooksModelViewSet)
router.register('authors', views.AuthorsModelViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/<int:pk>/', include(router.urls)),
]
