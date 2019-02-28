from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
import json
# from django.views.generic import View
# from django.http import HttpResponse
# from jwt_auth.mixins import JSONWebTokenAuthMixin

from django.views.decorators.http import require_http_methods


from django.views.decorators.csrf import csrf_exempt
from . import views


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

# class RestrictedView (JSONWebTokenAuthMixin,View):
#     def get(self,request):
#         data=json.dumps({
#             'foo':'bar'
#         })
#         return HttpResponse(data,content_type='application/json')


@csrf_exempt
def hook_receiver_view(request):

    if request.method == 'POST':
        # user_name = request.POST.get("user_name")
        # user_object = User.objects.get(user_name=user_name)
        # note_title = request.POST.get("note_title")
        # note_text = request.POST.get("data1")
        # received_json_data = json.loads(request.body)
        #  type(received_json_data)
        # note_text = json.loads(request.POST[data1])
        # note_title = json.loads(request.POST[note_title])
        # user_name = json.loads(request.POST[user_name])
        # user_name = received_json_data .get("user_name")
        # user_object = User.objects.get(user_name=user_name)
        # note_title = received_json_data .get("note_title")
        # note_text = received_json_data .get("data1")


        received_json_data = json.loads(request.body.decode("utf-8"))
        print(received_json_data)
        user_name = received_json_data["user_name"]
        user_object = User.objects.get(user_name=user_name)
        note_title = received_json_data["note_title"]
        note_text = received_json_data["data1"]
        note = NotesEntry(user_name=user_object, note_title=note_title, note_text=note_text)
        note.save()
        return JsonResponse({'display': 'Its a POST method'})
    else:
        return JsonResponse({'display': 'Its not a POST method'})