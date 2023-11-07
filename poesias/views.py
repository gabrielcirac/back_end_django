from django.contrib import messages
from poesias.forms import RegisterForm
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.urls import reverse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .models import Autor
from poesias.utils.fabrica import fazer_poema
from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
    return render(request, 'home.html')


def sobre_view(request):
    return render(request, 'sobre.html')


def blog_view(request):
    return render(request, 'blog.html')


def user_view(request, username):
    return HttpResponse(f'Nome do Usuário: {username}')


def poema_text(request, poema_id):
    return render(request, 'partial/poema_detail.html')


# Extends


def page_extends(request):
    return render(request, 'page_extends.html')


def principal(request):
    return render(request, "principal.html")


def sobre(request):
    return render(request, "sobre.html")


def poema_detail(request):
    poetry = fazer_poema()
    return render(request, 'poema_detail.html', {'poetry': poetry})


# Tag for
def poema_list(request):
    poesias = [fazer_poema() for _ in range(8)]
    return render(request, 'poema_list.html', {'poesias': poesias})


def search(request):
    query = request.GET.get('query', '').strip()

    # Supondo que estamos buscando filmes pelo nome
    autor = Autor.objects.filter(
        name__icontains=query
    ).order_by('-id')

    return render(request, 'search.html', {
        'first': f'Busca por "{autor[0]}"',
        'authors': autor,
    })

# Register Form


def register_view(request):
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            # processar dados se forem válidos
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            request.session['message'] = "Registro bem-sucedido!"
            return redirect('/')
    else:
        form = RegisterForm()

    return render(request, 'register_view.html', {'form': form})

# Login


def user_login_view(request):
    user = None
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        messages.success(request, "Logado com Sucesso")
        return redirect('/')
    else:
        messages.error(request, "Usuário ou Senha Invalidos")
    return render(request, 'login_2.html')


def login_form_view(request):
    user = None
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Logado com Sucesso")
                return redirect('/')
            else:
                messages.error(request, "Usuário ou Senha Inválidos")

    else:
        form = LoginForm()

    context = {'form': form}
    return render(request, 'login_3.html', context)


def user_logout_view(request):
    logout(request)
    # Após efetuar o logout, redireciona o usuário para a página de login ou homepage
    # Adiciona uma mensagem de sucesso
    messages.success(request, "Deslogado com sucesso!")
    return redirect(reverse('poesias:login_form'))
