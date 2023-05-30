import tempfile
from urllib import response
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from authentification.forms import LoginForm, RegisterForm
from shop.models import *
from mein.forms import *

def index(request):
    return render(request, "index.html")


def proects(request):
    return render(request, "proects.html")


def km(request):
    return render(request, "km.html")


def kozm(request):
    return render(request, "kozm.html")


def about(request):
    return render(request, "about-us.html")

from django.shortcuts import render
from django.views.generic import TemplateView
def home(request):
    return render(request, 'home.html')



from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

from authentification.forms import ContactForm
from django.core.mail import send_mail
from django.shortcuts import redirect


# kdgfgwlfgiuqwf
def send_email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():

            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, email, message, ['daryawaspd@gmail.com'])
            except BadHeaderError:
                return redirect('index.html')

            render(request, "email.html")
    else:
        form = ContactForm()
    return render(request, "email.html", {
        'form': form
    })

    # subject = request.POST.get("subject", "")
    # message = request.POST.get("message", "")
    # from_email = request.POST.get("from_email", "")
    # if subject and message and from_email:
    #     try:
    #         send_mail(subject, message, from_email, ["admin@example.com"])
    #     except BadHeaderError:
    #         return HttpResponse("Invalid header found.")
    #     return HttpResponseRedirect("/contact/thanks/")
    # else:
    #     # In reality we'd use a form class
    #     # to get proper validation errors.
    #     return HttpResponse("Make sure all fields are entered and valid.")


# def create_pdf(request):
#     product = Product.objects.all()
#     return render(request, "pdf.html", {"product": product})
#
#

def login_user(request):
    context = {'login_form': LoginForm()}

    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
            else:
                context = {
                    'login_form': login_form,
                    'attention': f'Пользователь с логином {username} и пароль не был найден !'
                }
        else:
            context = {
                'login_form': login_form,
            }

    return render(request, 'auth/login.html', context)


class RegisterView(TemplateView):
    template_name = 'auth/registration.html'

    def get(self, request):
        user_form = RegisterForm()
        context = {'user_form': user_form}
        return render(request, 'auth/registration.html', context)

    def post(self, request):
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            login(request, user)
            return redirect('index')

        context = {'user_form': user_form}
        return render(request, 'auth/registration.html', context)


def logout_user(request):
    logout(request)
    return redirect('index')


def test(request):
    obj = Bridge.objects.all()
    return render(request, "test.html", {"obj": obj})


def shedule(request):
    obj = WorkShedue.objects.all()
    return render(request, "shedule.html", {"obj": obj})


#
#
# # изменение данных в бд
def buy(request, id_object):
    obj = Bridge.objects.get(id_object=id_object)
    return render(request, "buy.html", {"obj": obj})

    # try:
    #     obj = Product.objects.get(id=id)
    #
    #     if request.method == "POST":
    #         product.name = request.POST.get("name")
    #         product.code = request.POST.get("code")
    #         product.save()
    #         return HttpResponseRedirect("/")
    #     else:
    #         return render(request, "buy.html", {"product": product})
    # except Product.DoesNotExist:
    #     return HttpResponseNotFound("<h2>Product not found</h2>")


from reportlab.pdfgen import canvas
from django.http import HttpResponse


def getpdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'
    p = canvas.Canvas(response)
    p.setFont("Times-Roman", 55)
    p.drawString(100, 700, "")
    p.showPage()
    p.save()
    return response
