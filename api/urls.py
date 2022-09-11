from django.urls import path, include
from rest_framework import routers
from .views import TaskViewSet, ProfileViewSet, CategoryViewSet, ListUserView, LoginUserView, CreateUserView

router = routers.DefaultRouter()
router.register('category', CategoryViewSet)
router.register('profile', ProfileViewSet)
router.register('tasks', TaskViewSet)

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
    path('users/', ListUserView.as_view(), name='users'),
    path('loginuser/', LoginUserView.as_view(), name='loginuser'),
    path('', include(router.urls))
]