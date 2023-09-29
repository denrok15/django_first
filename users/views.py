from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from users.forms import UserCreationForm


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
    return render(request, 'Teoria.html')


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
