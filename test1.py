import os

from django.utils import timezone

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "meiduo_mall.settings.settings")
a = timezone.now().strftime('%Y%m%d%H%M%S')
# b = a.now()
print(a)
