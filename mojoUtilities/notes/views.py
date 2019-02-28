from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
# import json
# from django.views.generic import View
# from jwt_auth.mixins import JSONWebTokenAuthMixin

from django.views.decorators.http import require_http_methods


from django.views.decorators.csrf import csrf_exempt


from .models import User, NotesEntry
# Create your views here.
def index(request):
    try:
        session_user_name = request.session['user_name']
        return HttpResponseRedirect('/notes/@%s/dashboard' %(session_user_name))
    except:
        session_data = [(key, value) for key, value in request.session.items()]
        context = {
            'session_data': session_data,
        }
        return render(request, 'notes/login.html', context)

def userLogin(request):
        user_name = request.POST.get("user_name")
        user_password = request.POST.get("user_password")
        user_object = User.objects.filter(user_name = user_name)
        possible_passwords = [i.user_password for i in user_object]
        context = {
            'user_name': user_name,
        }
        if user_password in possible_passwords:
            request.session['user_name'] = user_name
            return HttpResponseRedirect('/notes/@%s/dashboard' %(user_name))
        else:
            return HttpResponse("User not found")
    

def userLogout(request, user_name):
    try:
        session_user_name = request.session['user_name']
        if (user_name == session_user_name):
            del request.session['user_name']
            return HttpResponseRedirect(reverse('notes:index'))
        else:
            return HttpResponse("user_name does not match with the session_user_name")
    except:
        return HttpResponse("Cannot access session_user_name")
        

def userDashboard(request, user_name):
    try:
        session_user_name = request.session['user_name']
        if (user_name == session_user_name):
            pass
        else:
            user_name = session_user_name
            return HttpResponse("session_user_name does not match with user_name")
        user_object = User.objects.get(user_name = user_name)
        user_notes = NotesEntry.objects.filter(user_name = user_object)
        session_data = [(key, value) for key, value in request.session.items()]
        context = {
            'user_name': user_name,
            'user_notes': user_notes,
            'session_data': session_data,
            # 'error_msg': error_msg,
        }
        return render(request, 'notes/user_dashboard.html', context)
    except:
        return HttpResponse("Cannot access session_user_name")


def addNewNote(request, user_name):
    try:
        session_user_name = request.session['user_name']
        if (user_name == session_user_name):
            pass
        else:
            user_name = session_user_name
            return HttpResponse("session_user_name does not match with user_name")
        context = {
            'user_name': user_name,
        }
        return render(request, 'notes/add_new_note.html', context)
    except:
        return HttpResponse("Cannot access session_user_name")


def addNote(request, user_name):
    try:
        session_user_name = request.session['user_name']
        if (user_name == session_user_name):
            pass
        else:
            user_name = session_user_name
            return HttpResponse("session_user_name does not match with user_name")
        user_object = User.objects.get(user_name = user_name)
        note_title = request.POST.get("note_title")
        note_text = request.POST.get("note_text")
        note = NotesEntry.objects.create(user_name=user_object, note_title= note_title, note_text = note_text)
        context = {
            'user_name': user_name,
        }
        return HttpResponseRedirect('/notes/@%s/dashboard' %(user_name))
    except:
        return HttpResponse("Cannot access session_user_name")

# class RestrictedView (JSONWebTokenAuthMixin,View):
#     def get(self,request):
#         data=json.dumps({
#             'foo':'bar'
#         })
#         return HttpResponse(data,content_type='application/json')


@csrf_exempt
def hook_receiver_view(request):
    print(request.method)
    if request.method == 'POST':
        # print(request.POST.get("data1"))
        # print(request.POST.get("note_title"))
        # print(request.POST.get("user_name"))
        user_name=request.POST.get("user_name")
        user_object =User.objects.get(user_name=user_name)
        note_title=request.POST.get("note_title")
        note_text= request.POST.get("data1")
        note=NotesEntry(user_name=user_object,note_title=note_title,note_text=note_text)
        note.save()
        return JsonResponse({'foo': 'bar'})

    else:
        return JsonResponse({'abc': 'cdf'})