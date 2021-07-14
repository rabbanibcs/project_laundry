from django.shortcuts import render
from laundry.models import Orders, OrderItems
from django_xhtml2pdf.utils import pdf_decorator


@pdf_decorator(pdfname='new_filename.pdf')
def create_invoice(request, id):
    order = Orders.objects.get(id=id)
    items = OrderItems.objects.filter(order=order)
    context = {'order': order, 'items': items}
    return render(request, 'invoice.html', context)
