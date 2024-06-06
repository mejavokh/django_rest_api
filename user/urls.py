from django.urls import path
from user.views import UserListAPIVew


urlpatterns = [
    path('user/', UserListAPIVew.as_view(), name='user')
]

