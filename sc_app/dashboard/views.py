from django.shortcuts import render
from dashboard.models import User, Company, SocialProfile, Service

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, "dashboard/index.html")


@login_required
def dashboard(request):
    # print(request.user.userprofile.company.subscriptions.all())
    try:
        qs = request.user.userprofile.company.subscriptions.all()
    except:
        qs = None

    context = {"subscription_list": qs}

    return render(request, "dashboard/dashboard.html", context)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("index")


def user_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(email=email, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseDirect("dashboard")
            else:
                return HttpResponse("Account isn't active")
        else:
            print("Someone failed at logging in")
            print("username: {} and password {}".format(username, password))
            return HttpResponse("Invalid logins")
    else:
        return render(request, "dashboard.html", {})
