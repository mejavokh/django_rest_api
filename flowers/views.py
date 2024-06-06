from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import *
from .serializers import *
# Create your views here.


class FlowerListAPIView(ListAPIView):
    queryset = Flowers.objects.only('id', 'title', 'occasion', 'price')
    serializer_class = FlowerListAPISerializer


class FlowerDetailAPIView(RetrieveAPIView):
    queryset = Flowers.objects.all()
    serializer_class = FlowersDetailAPISerializer
