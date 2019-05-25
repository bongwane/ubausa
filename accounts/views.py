from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader


def user_login(request):
    username = request.POST["email_address"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    response = {}
    if user is not None:
        login(request, user)
        response["logged_in"] = True
        response["username"] = username
        response["first_name"] = user.first_name

    else:
        # user authentication failure
        response["logged_in"] = False

    return redirect("backend.index")

def admin_login(request):
    username = request.POST["email_address"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    response = {}
    if user is not None:
        login(request, user)
        response["logged_in"] = True
        response["username"] = username
        response["first_name"] = user.first_name

    else:
        # user authentication failure
        response["logged_in"] = False

    return redirect("backend.admin")
