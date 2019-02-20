from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.response import Response

from goods.models import SKU, GoodsCategory
from goods.serializers import SKUSerializer, ChannelSerializer, CategorySerializer


# 请求方式： GET /categories/(?P<category_id>\d+)/skus?page=xxx&page_size=xxx&ordering=xxx
class SKUListView(ListAPIView):
    serializer_class = SKUSerializer
    filter_backends = (OrderingFilter,)
    ordering_fields = ('create_time', 'price', 'sales')

    # 可以用这种方法得到url参数
    # queryset = SKU.objects.filter(is_launched=True, category_id=category_id)
    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return SKU.objects.filter(category_id=category_id, is_launched=True)


class CategoryView(GenericAPIView):
    """
    商品列表页面包屑导航
    """
    queryset = GoodsCategory.objects.all()

    def get(self, request, pk=None):
        ret = dict(
            cat1='',
            cat2='',
            cat3=''
        )
        category = self.get_object()
        if category.parent is None:
            # 当前类别为一级类别
            ret['cat1'] = ChannelSerializer(category.goodschannel_set.all()[0]).data
        elif category.goodscategory_set.count() == 0:
            # 当前类别为三级
            ret['cat3'] = CategorySerializer(category).data
            cat2 = category.parent
            ret['cat2'] = CategorySerializer(cat2).data
            ret['cat1'] = ChannelSerializer(cat2.parent.goodschannel_set.all()[0]).data
        else:
            # 当前类别为二级
            ret['cat2'] = CategorySerializer(category).data
            ret['cat1'] = ChannelSerializer(category.parent.goodschannel_set.all()[0]).data

        return Response(ret)
