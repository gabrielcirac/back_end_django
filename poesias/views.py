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
