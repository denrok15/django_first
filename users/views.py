from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from users.forms import UserCreationForm
from .forms import UserProfileForm, UserEditForm
from .models import UserProfile


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def vved(request):
    return render(request, 'vvedenie.html')


def liney(request):
    return render(request, 'liney.html')


def registr(request):
    return render(request, 'registr.html')


def profile(request):
    return render(request, 'profile2.html')


def testir(request):
    return render(request, 'vvedenie.html')


def teoria(request):
    return render(request, 'kyrs.html')


def teorialin(request):
    return render(request, 'teoria/teoria.html')


def properties(request):
    return render(request, 'teoria/property.html')


def grafics(request):
    return render(request, 'functions/obs.html')


def grafkyrs(request):
    return render(request, 'kyrs5.html')


def parabola(request):
    return render(request, 'functions/parabola.html')


def giperbola(request):
    return render(request, 'functions/giperbola.html')


def kx(request):
    return render(request, 'functions/kx.html')


def trig(request):
    return render(request, 'functions/trig.html')


def log(request):
    return render(request, 'functions/log.html')


def bank(request):
    return render(request, 'bank.html')


def kyrs2(request):
    return render(request, 'kyrs2.html')

def kyrs3(request):
    return render(request, 'kyrs3.html')

def kyrs4(request):
    return render(request, 'kyrs4.html')

def kyrs5(request):
    return render(request, 'kyrs5.html')
def lnteor(request):
    return render(request,'teoria/ln.html')
def prln(request):
    return render(request,'practica/practicalin.html')
def grprac(request):
    return render(request,'practica/graf.html')
def kvprac(request):
    return render(request,'practica/kvadrpract.html')
def kvteor(request):
    return render(request,'teoria/kvadrat.html')
class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

def edit_profile(request):
    user = request.user
    profile, created = UserProfile.objects.get_or_create(user=user)
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')  # URL name для страницы профиля
    else:
        user_form = UserEditForm(instance=user)
        profile_form = UserProfileForm(instance=profile)

    return render(request, 'Edit.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })
# <details>
#    <summary>
#       <h2 class = "fs-2 fw-bold">Линейные конструкции:</h2>
#    </summary>
#   <a class="text-decoration-none text-dark" href="{% url 'liney' %}"><p class="fs-4">Теория</p></a>
#  <a href="{% url 'liney' %}"><p class="fs-4">Примеры решения</p></a>
#   <a class="me-2 py-2 text-dark text-decoration-none" href="{% url 'liney' %}"><p>Практика</p></a>
#  <a class="me-2 py-2 text-dark text-decoration-none" href="{% url 'liney' %}"><p>Задачи реального егэ</p></a>
#   <a class="me-2 py-1 text-dark text-decoration-none" href="{% url 'liney' %}"><p>Проверочная работа</p></a>
# </details>
