from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app_todo.views import TodoView, TagViewSet

Router = routers.DefaultRouter()
Router.register(r"todos", TodoView, "todos")
Router.register(r"tags", TagViewSet, "tags")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(Router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
