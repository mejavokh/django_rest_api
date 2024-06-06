from rest_framework import serializers

from common.models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    text = serializers.CharField(max_length=120)

    class Meta:
        model = Feedback
        fields = ['id', 'text']
