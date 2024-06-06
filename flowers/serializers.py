from rest_framework import serializers

from common.serializers import MediaURLSerializer
from flowers.models import *


class FlowerImageSerializer(serializers.ModelSerializer):
    image = MediaURLSerializer()

    class Meta:
        model = FlowerImage
        exclude = ('flower',)
        read_only_fields = ['id', 'image']


class FlowerListAPISerializer(serializers.Serializer):
    flower_image = FlowerImageSerializer(many=True)

    class Meta:
        model = Flowers
        fields = ('id', 'title', 'to-whom', 'price')


class FlowersDetailAPISerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    occasion = serializers.CharField()
    price = serializers.IntegerField()

    class Meta:
        model = Flowers
        read_only_fields = ['id', 'title', 'occasion', 'to_whom', 'desc', 'feedback', 'tags']




