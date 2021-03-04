from celery import  shared_task
from django.core.mail import send_mail
from .models import Order




# @task is deprecated
# https://docs.celeryproject.org/en/stable/getting-started/first-steps-with-celery.html#tut-celery
# https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html#using-celery-with-django
@shared_task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.first_name},\n\n' \
    f'You have successfully placed an order.' \
    f'Your order ID is {order.id}.'
    mail_sent = send_mail(subject,
                            message,
                            'admin@myshop.com',
                            [order.email])
    return mail_sent