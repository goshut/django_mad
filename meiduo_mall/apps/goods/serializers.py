from rest_framework import serializers

from goods.models import SKU, GoodsChannel, GoodsCategory


class SKUSerializer(serializers.ModelSerializer):
    class Meta:
        model = SKU
        fields = ('id', 'name', 'price', 'default_image_url', 'comments')


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsChannel
        fields = ['group_id', "category", 'url', 'sequence']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = ['parent', 'name']

