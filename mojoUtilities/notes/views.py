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
    user_object = User.objects.get(user_name = user_name)
    user_notes = NotesEntry.objects.filter(user_name = user_object)
    context = {
        'user_name': user_name,
        'user_notes': user_notes,
    }
    return render(request, 'notes/user_dashboard.html', context)


def addNewNote(request, user_name):
    context = {
        'user_name': user_name,
    }
    return render(request, 'notes/add_new_note.html', context)


def addNote(request, user_name):
    user_object = User.objects.get(user_name = user_name)
    note_title = request.POST.get("note_title")
    note_text = request.POST.get("note_text")
    note = NotesEntry(user_name=user_object, note_title= note_title, note_text = note_text)
    note.save()
    context = {
        'user_name': user_name,
    }
    return HttpResponseRedirect('/notes/@%s/dashboard' %(user_name))