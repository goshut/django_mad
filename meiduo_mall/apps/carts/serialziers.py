from rest_framework import serializers

from goods.models import SKU


class CartSerializer(serializers.Serializer):
    sku_id = serializers.IntegerField(label='sku id ', min_value=1)
    count = serializers.IntegerField(label='数量 ', min_value=1)
    selected  = serializers.BooleanField(label='是否勾选', default=True)

    def validate(self, data):
        try:
            sku = SKU.objects.get(id=data['sku_id'])
        except SKU.DoesNotExist:
            raise serializers.ValidationError('商品不存在')

        return data


class CartSKUSerializer(serializers.ModelSerializer):
    selected = serializers.BooleanField(label='是否勾选')
    count = serializers.IntegerField(label='数量 ')

    class Meta:
        model = SKU
        fields = ['id', 'count', 'default_image_url', 'price', 'selected', 'name']


