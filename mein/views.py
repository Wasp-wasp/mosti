from urllib import response

from shop.models import Product
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView

from django.shortcuts import render, get_object_or_404
import jinja2
import pdfkit
from datetime import datetime

import pdfkit
from io import BytesIO

from django.template.loader import get_template
from django.http import HttpResponse
from django.template import loader


class UserListView(ListView):
    model = Product
    template_name = 'templates/buy.html'


def users_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    product = get_object_or_404(Product, pk=pk)

    template_path = "pdf.html"
    context = {'product': product}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    # to directly download the pdf we need attachment
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    # to view on browser we can remove attachment
    response['Content-Disposition'] = 'filename="report.pdf"'

    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about-us.html")


def create_pdf(request):
    product = Product.objects.all()
    return render(request, "pdf.html", {"product": product})


def test(request):
    product = Product.objects.all()
    return render(request, "index.html", {"product": product})


# изменение данных в бд
def buy(request, id):
    try:
        product = Product.objects.get(id=id)

        if request.method == "POST":
            product.name = request.POST.get("name")
            product.code = request.POST.get("code")
            product.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "buy.html", {"product": product})
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")
