from django.http import HttpResponse
from django.template import loader

from django.shortcuts import render


def index(request):
    context = {}
    if request.user.is_authenticated:
        template = loader.get_template("backend/index.html")
        return HttpResponse(template.render(context, request))
    else:
        # redirect to login page
        template = loader.get_template("accounts/login.html")
        return HttpResponse(template.render(context, request))

def admin_index(request):
    context = {}
    if request.user.is_authenticated:
        template = loader.get_template("backend/admin/index.html")
        return HttpResponse(template.render(context, request))
    else:
        # redirect to login page
        template = loader.get_template("accounts/admin/login.html")
        return HttpResponse(template.render(context, request))
