from django.urls import path, include
from .views import TaskListAPIView, TaskDetailAPIView, TaskViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    # path('tasks/', TaskListAPIView.as_view(), name='task-list'),
    # path('tasks/<int:pk>/', TaskDetailAPIView.as_view(), name='task-detail')
    path('', include(router.urls))
]
