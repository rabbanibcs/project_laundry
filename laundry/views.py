from django.shortcuts import render
from laundry.models import Orders, OrderItems
from django_xhtml2pdf.utils import pdf_decorator


@pdf_decorator(pdfname='invoice.pdf')
def create_invoice(request, pk):
    order = Orders.objects.get(id=pk)
    items = OrderItems.objects.filter(order=order)

    context = {'order': order, 'items': items}
    return render(request, 'invoice.html', context)
