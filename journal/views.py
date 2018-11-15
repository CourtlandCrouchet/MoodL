from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import render

from .models import Entries
from .forms import EntryForm

def index(request):
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
            new_entry = Entries.create(entry_text)
            # redirect to a new URL:
            return HttpResponseRedirect('submitted')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = EntryForm()

    return render(request, 'journal/new_entry.html', {'form': form})
def submitted(request):
    template = loader.get_template('journal/get_entry/submitted.html')
    return HttpResponse(render(request, 'journal/get_entry/submitted.html'))
def graph(request):
    moods = Entries.objects.get(pk=7)
    template = loader.get_template('journal/graph.html')
    context = {
        'moods': moods,
    }
    return HttpResponse(template.render(context, request))
