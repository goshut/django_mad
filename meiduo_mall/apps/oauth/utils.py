from itsdangerous import TimedJSONWebSignatureSerializer as TJSS, BadData

from meiduo_mall.settings import settings
from oauth import constants


def generate_save_user_token(openid):
    """
    生成保存用户数据的token
    :param openid: 用户的openid
    :return: token
    """
    serializer = TJSS(settings.SECRET_KEY, expires_in=constants.SAVE_QQ_USER_TOKEN_EXPIRES)
    data = {'openid': openid}
    token = serializer.dumps(data)
    return token.decode()


def check_save_user_token(access_token):
    """
    检验保存用户数据的token
    :param token: token
    :return: openid or None
    """
    serializer = TJSS(settings.SECRET_KEY, expires_in=constants.SAVE_QQ_USER_TOKEN_EXPIRES)
    try:
        data = serializer.loads(access_token)
    except BadData:
        return None
    else:
        return data.get('openid')
