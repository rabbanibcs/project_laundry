from .models import Orders


def extras(request):
    pending = Orders.objects.filter(order_status='pending').count()
    processing = Orders.objects.filter(order_status='processing').count()

    return {'pending': pending,'processing':processing}