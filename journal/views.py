from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import render

from .models import Entries
from .forms import EntryForm

from django.core import serializers

def index(request): #OBSOLETE, used for reference
    latest_entries_list = Entries.objects.order_by('-submission_date')[:5]
    template = loader.get_template('journal/index.html')
    context = {
        'latest_entries_list': latest_entries_list,
    }
    return HttpResponse(template.render(context, request))

def get_entry(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EntryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
        # process the data in form.cleaned_data as required
            entry_text = form.cleaned_data['entry_form']
            #user_id = user ID of the current session
            user_id = request.user
            #Use Entries create method to analyze and store the Entry
            new_entry = Entries.create(entry_text, user_id)
            # redirect to a new URL:
            return HttpResponseRedirect('graph/'+str(new_entry.id))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = EntryForm()
    user_id = request.user
    data = serializers.serialize("python", Entries.objects.filter(user_ID = user_id))
    moods = Entries.objects.get(pk=0)
    context = {
        'form': form,
        'data': data,
        'moods': moods,
    }
    return render(request, 'journal/new_entry.html', context)
def submitted(request): #OBSOLETE, used for testing
    user_id = request.user
    data = serializers.serialize("python", Entries.objects.filter(user_ID = user_id))
    context = {
        'user_id': user_id,
        'data': data,
    }
    template = loader.get_template('journal/get_entry/submitted.html')
    return HttpResponse(template.render(context,request))


def graph(request, id): #OBSOLETE, used for testing
    user_id = request.user
    data = serializers.serialize("python",Entries.objects.filter(user_ID = user_id))
    moods = Entries.objects.get(pk=id)
    template = loader.get_template('journal/graph.html')
    context = {
        'user_id': user_id,
        'moods': moods,
        'data': data,
    }
    return HttpResponse(template.render(context, request))
