from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('HOME')

def sobre(request):
    return HttpResponse('SOBRE')

def contato(request):
    return HttpResponse('CONTATO')
