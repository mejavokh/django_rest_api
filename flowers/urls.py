from django.urls import path

from flowers.views import *


urlpatterns = [
    path('flower/', FlowerListAPIView.as_view(), name='flower'),
    path('<int:pk>/', FlowerDetailAPIView.as_view(), name='flower-detail')
]

