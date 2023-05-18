from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from authentification.forms import LoginForm, RegisterForm
from shop.models import Object


def about(request):
    return render(request, "about-us.html")


def test(request):
    obj = Object.objects.all()
    return render(request, "test.html", {"obj": obj})


def pdf(request):
    product = Object.objects.all()
    return render(request, {"product": product})


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


from reportlab.pdfgen import canvas
from django.http import HttpResponse


def getpdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'
    p = canvas.Canvas(response)
    p.setFont("Times-Roman", 55)
    p.drawString(100, 700, "Hello, Javatpoint.")
    p.showPage()
    p.save()
    return response
