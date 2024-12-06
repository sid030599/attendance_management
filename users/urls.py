from django.urls import path
from .views import UserListView, LoginView

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('login/', LoginView.as_view(), name='login'),
]
