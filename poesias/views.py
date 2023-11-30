from django.views.generic.edit import FormView
from .forms import RegisterForm  # Importe seu RegisterForm
from django.urls import reverse_lazy
from poesias.models import Livro
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
from django.views.generic import TemplateView, View


class HomeView(TemplateView):
    template_name = 'home.html'


class SobreView(TemplateView):
    template_name = 'sobre.html'


class BlogView(TemplateView):
    template_name = 'blog.html'


class UserView(View):
    def get(self, request, username):
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


def lista_livros(request):
    livros = Livro.objects.filter()
    return render(request, 'lista_livros.html', {'livros': livros})


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


class RegisterView(FormView):
    template_name = 'register.html'  # Nome do template que será usado
    form_class = RegisterForm
    success_url = reverse_lazy('/')  # URL para redirecionar após o sucesso

    def form_valid(self, form):
        # Este método é chamado quando dados válidos são postados no formulário
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()

        # Configurando uma mensagem para a sessão
        self.request.session['message'] = "Registro bem-sucedido!"
        return super().form_valid(form)


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
