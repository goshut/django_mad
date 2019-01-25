from rest_framework import serializers

from . import models


class AreaSerializer(serializers.ModelSerializer):
    """
    行政区划信息序列化器
    """
    class Meta:
        model = models.Area
        fields = ['id', 'name']


class SubAreaSerializer(serializers.ModelSerializer):
    """
    子行政区划信息序列化器
    """
    subs = AreaSerializer(many=True, read_only=True)

    class Meta:
        model = models.Area
        fields = ['id', 'name', 'subs']
