from random import randint

from django.shortcuts import render
from django_redis import get_redis_connection
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from meiduo_mall.libs.yuntongxun.sms import CCP
import logging

logger = logging.getLogger('django')


# url('^sms_codes/(?P<mobile>1[3-9]\d{9})/$', views.SMSCodeView.as_view()),
class SMSCodeView(APIView):
    """
    发送短信验证码
    mobile, image_code_id, text
    """
    def get(self, request, mobile):
        redis_sms = get_redis_connection('verify_codes')
        send_flag = redis_sms.get('send_flag_%s' % mobile)
        if send_flag:
            return Response({"message": "发送短信过于频繁"}, status=status.HTTP_400_BAD_REQUEST)
        sms_code = '%06d' % randint(0, 999999)
        logger.info(sms_code)
        # CCP().send_template_sms(mobile, [sms_code, 300 // 60], 1)
        redis_sms.setex('sms_%s' % mobile, 300, sms_code)
        return Response({'message': 'OK',
                         'sms_code': sms_code})

