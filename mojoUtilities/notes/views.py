from django.shortcuts import render
from django.http import HttpResponse

from .models import User, NotesEntry
# Create your views here.
def index(request):
	return render(request, 'notes/index.html')


def userLogin(request):
    user_name = request.POST.get("user_name")
    user_password = request.POST.get("user_password")
    user_object = User.objects.filter(user_name = user_name)
    possible_passwords = [i.user_password for i in user_object]
    if password in possible_passwords:
        return redirect('notes:dashboard', user_name=user_name)
    else:
        return HttpResponse("User not found")


def userDashboard(request, user_name):
	return render(request, 'notes/dashboard.html')