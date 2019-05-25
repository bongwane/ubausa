from django.http import HttpResponse
from django.template import loader

from django.shortcuts import render
from .models import Card

def index(request):
    context = {}
    cards = Card.objects.all()
    context["cards"] = cards

    template = loader.get_template("backend/admin/cards.html")
    return HttpResponse(template.render(context, request))
