from django.urls import path

from common.views import ConfigView

urlpatterns = [
    path('config/', ConfigView.as_view(), name='config')
]
