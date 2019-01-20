from celery_tasks.sms.yuntongxun.sms import CCP
from celery_tasks.main import celery_app


@celery_app.task()
def send_sms_code(mobile, sms_code, time_min, template_id):
    CCP().send_template_sms(mobile, [sms_code, time_min], template_id)
