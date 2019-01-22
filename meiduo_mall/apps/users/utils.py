import re

from django.contrib.auth.backends import ModelBackend
from rest_framework.response import Response

from users.models import User


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'username': user.username,
        'user_id': user.id
    }


def get_user_by_account(account):
    """根据传⼊的账号获取⽤户信息"""
    try:
        if re.match('^1[3-9]\d{9}$', account):
        # ⼿机号登录
            user = User.objects.get(mobile=account)
        else:
        # ⽤户名登录
            user = User.objects.get(username=account)
    except User.DoesNotExist:
        return None
    else:
        return user


class UsernameMobileAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = get_user_by_account(username)
        if user and user.check_password(password):
            return user

