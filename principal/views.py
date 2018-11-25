from django.shortcuts import render, render_to_response
from django.template.context_processors import csrf
from django.contrib.auth import login as auth_login, logout
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views import generic

def main_base_view(request):
    dictionary = dict(request=request)
    dictionary.update(csrf(request))
    return render_to_response('main/main_base.html', dictionary)


def login(request):
    if request.method == 'POST':
        username = request.POST['u']
        password = request.POST['p']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request=request, user=user)
            dictionary = dict(request=request)
            dictionary.update(csrf(request))
            return render_to_response('journal/new_entry.html', dictionary)
        else:
            msg_to_html = custom_message('Invalid Credentials', TagType.danger)
            dictionary = dict(request=request, messages = msg_to_html)
            dictionary.update(csrf(request))
        return render_to_response('main/main_base.html', dictionary)


#def signup(request):
 #   if request.method == 'POST':
  #      username = request.POST.get('name')
   #     pass_1 = request.POST.get('password1')
    #    pass_2 = request.POST.get('password2')
     #      user = User.objects.create_user(username=username, password=pass_1)
      #      dictionary = dict(request=request)
       #     dictionary.update(csrf(request))
        #    return render_to_response('main/main_base.html', dictionary)
        #else:
         #   msg_to_html = custom_message('Invalid Credentials', TagType.danger)
          #  dictionary = dict(request=request, messages=msg_to_html)
           # dictionary.update(csrf(request))
        #return render_to_response('account/signup.html', dictionary)

class signup(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('get_entry')
    template_name = 'signup.html'

# this def is if you want to change the user's password
def update_pwd(username, pwd):
    user_model = User.objects.get(username=username)
    user_model.set_password(pwd)
    user_model.save()


def logout_view(request):
    logout(request)
    dictionary = dict(request=request)
    dictionary.update(csrf(request))
    return render_to_response('main/main_base.html', dictionary)


class Messages:
    def __init__(self):
        self.message = ''

    message = ''
    tag = ''


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