from django.db.models.signals import post_save
from .models import Orders
from django.dispatch import receiver


@receiver(post_save,sender=Orders)
def status_update(sender=Orders,**kwargs):
    print('signal received')
    print(f'{kwargs}')
    print(kwargs['instance'])
    print(kwargs['created'])
    print(kwargs['update_fields'])
    order=kwargs['instance']
    if order.order_status == 'processing':
        print('processing')
    if order.order_status == 'shipping':
        print('shipping')
    if order.order_status == 'cancel':
        print('cancel')



