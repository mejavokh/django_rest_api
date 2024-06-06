from django.urls import path

from .views import FeedbackAPIView

urlpatterns = [
    path('reviews/', FeedbackAPIView.as_view(), name='reviews')
]





