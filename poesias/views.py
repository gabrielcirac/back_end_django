from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
    return HttpResponse("HOME")


def contato_view(request):
    return HttpResponse("Página de Contatos")


def usuario_view(request, nome):
    return HttpResponse(f"Página do Usuario: {nome}")


def poesia_view(request, poesia):
    return HttpResponse(f"Isso é uma poesia: {poesia}")


def vendas_view(request, venda):
    return HttpResponse(f"Aqui você pode comprar tudo: {venda}")
