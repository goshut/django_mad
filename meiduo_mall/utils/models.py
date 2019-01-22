from django.db import models


class BaseModel(models.Model):
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        abstract = True  # 说明是抽象模型类, 用于继承使用，数据库迁移时不会创建BaseModel的表
