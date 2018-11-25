from django.shortcuts import render, render_to_response
from django.template.context_processors import csrf
from django.contrib.auth import login as auth_login, logout
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views import generic

# this calls the main page, before you login.
def main_base_view(request):
    dictionary = dict(request=request)
    dictionary.update(csrf(request))
    return render_to_response('main/main_base.html', dictionary)

# this calls the login drop down box
# it checks if the user is using the correct username and password combo
# if the user logs in correctlly, it will link the page to the user log page
# else it will return the user to the homepage
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

# this will direct the user to signup page, and after a user is created, it will bring user
# to the user log page for them to start entering their entry.
class signup(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('get_entry')
    template_name = 'signup.html'

#def about_page_view(request):
 #   return render(request, 'about.html')

# this def is if you want to change the user's password
def update_pwd(username, pwd):
    user_model = User.objects.get(username=username)
    user_model.set_password(pwd)
    user_model.save()

# this def when you log out it brings you to to the home page
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

# different alert messages
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