from rest_framework.generics import ListAPIView

from .serializers import FeedbackSerializer
from common.models import Feedback


class FeedbackAPIView(ListAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer





