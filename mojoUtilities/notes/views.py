from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import User, NotesEntry
# Create your views here.
def index(request):
	return render(request, 'notes/login.html')


def userLogin(request):
    user_name = request.POST.get("user_name")
    user_password = request.POST.get("user_password")
    user_object = User.objects.filter(user_name = user_name)
    possible_passwords = [i.user_password for i in user_object]
    context = {
        'user_name': user_name,
    }
    if user_password in possible_passwords:
        return HttpResponseRedirect('/notes/@%s/dashboard' %(user_name))
    else:
        return HttpResponse("User not found")


def userDashboard(request, user_name):
    context = {
        'user_name': user_name,
    }
    return render(request, 'notes/user_dashboard.html', context)