from django.shortcuts import render, render_to_response
from django.template.context_processors import csrf
from django.contrib.auth import login as auth_login, logout
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views import generic



#this brings up the main home page.
def main_base_view(request):
    dictionary = dict(request=request)
    dictionary.update(csrf(request))
    return render_to_response('main/main_base.html', dictionary)

#this def the login request, when the user successfully logs in
#they will be linked to the user log page (new_entry)
#when they fails to login, they will be brought to the main page.
def login(request):
    if request.method == 'POST':
        username = request.POST['u']
        password = request.POST['p']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request=request, user=user)
            dictionary = dict(request=request)
            dictionary.update(csrf(request))
            return HttpResponseRedirect('../journal/new_entry')
        else:
            msg_to_html = custom_message('Invalid Credentials', TagType.danger)
            dictionary = dict(request=request, messages = msg_to_html)
            dictionary.update(csrf(request))
        return render_to_response('main/main_base.html', dictionary)

#this class will generate the signup page that django provides.
#and after the user creates a new account, they will be linked to
#the user log page (get_entry)
#subclassing the generic class-based view CreateView in the signup class
#we specify the use of the built-in UserCreationForm.
#reverse_lazy because that for all generic class-based views the urls are
#not loaded when the file is imported, so we use the lazy form of revers
#rather than reverse.
class signup(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('get_entry')
    template_name = 'signup.html'

#this links the user to the about page.
def about(request):
    if request.user.id == None:
        return HttpResponseRedirect('..')
    else:
        return render(request, 'help.html')

# this def is if you want to change the user's password


def update_pwd(username, pwd):
    user_model = User.objects.get(username=username)
    user_model.set_password(pwd)
    user_model.save()

#this takes affect when the user logs out, and they will be linked to the main page.
def logout_view(request):
    logout(request)
    dictionary = dict(request=request)
    dictionary.update(csrf(request))
    return HttpResponseRedirect('..')


class Messages:
    def __init__(self):
        self.message = ''

    message = ''
    tag = ''

#these are the different levels of the alert.
def custom_message(message, tag):
    # 1.- success, 2.-info, 3.- warning 4.- danger
    msg = Messages()
    if tag == 0:
        msg.tag = "alert alert-success"
    elif tag == 1:
        msg.tag = "alert alert-info"
    elif tag == 2:
        msg.tag = "alert alert-warning"
    else:
        msg.tag = "alert alert-danger"

    msg.message = message
    return msg


class TagType:
    def __init__(self):
        pass

    success, info, warning, danger = range(4)