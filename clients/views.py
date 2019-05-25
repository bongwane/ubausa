from django.http import HttpResponse
from django.template import loader

from django.shortcuts import render
from .models import Client

def index(request):
    context = {}
    clients = Client.objects.all()
    context["clients"] = clients
    template = loader.get_template("backend/admin/clients.html")
    return HttpResponse(template.render(context, request))
