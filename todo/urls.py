from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app_todo.views import TodoView, TagViewSet

Router = routers.DefaultRouter()
Router.register(r'todos', TodoView, 'todos')
Router.register(r'tags', TagViewSet, 'tags')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(Router.urls)),
]
