from decimal import Decimal

from django.utils import timezone
from rest_framework import serializers

from goods.models import SKU
from orders.models import OrderInfo


class CartSKUSerializer(serializers.ModelSerializer):
    """
    购物车商品数据序列化器
    """
    count = serializers.IntegerField(label='数量')

    class Meta:
        model = SKU
        fields = ('id', 'name', 'default_image_url', 'price', 'count')


class OrderSettlementSerializer(serializers.Serializer):
    """
    订单结算数据序列化器
    """
    freight = serializers.DecimalField(label='运费', max_digits=10, decimal_places=2)
    skus = CartSKUSerializer(many=True)


class SaveOrderSerializer(serializers.ModelSerializer):
    """
    下单数据序列化器
    """

    class Meta:
        model = OrderInfo
        fields = ('order_id', 'address', 'pay_method')
        read_only_fields = ('order_id',)
        extra_kwargs = {
            'address': {
                'write_only': True,
                'required': True,
            },
            'pay_method': {
                'write_only': True,
                'required': True
            }
        }

    def create(self, validated_data):
        user = self.context['request'].user
        order_id = timezone.now().strftime('%Y%m%D%H%M%S') + '%09d' % user.id

        order = OrderInfo.objects.create(
            order_id=order_id,
            user=user,
            address=validated_data.get('address'),
            total_count=0,
            total_amount=Decimal(0),
            freight=Decimal(0),
            pay_method=validated_data['pay_method'],
            status=OrderInfo.ORDER_STATUS_ENUM['UNSEND'] if validated_data['pay_method'] == OrderInfo.PAY_METHODS_ENUM['CASH'] else OrderInfo.ORDER_STATUS_ENUM['UNPAID'],
        )
