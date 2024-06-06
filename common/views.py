from rest_framework.generics import RetrieveAPIView

from common.models import *
from common.serializers import *


class ConfigView(RetrieveAPIView):
    serializer_class = ConfigSerializer
    queryset = CommonSettings.objects.all()

    def get_object(self):
        return CommonSettings.objects.first()


