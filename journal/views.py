from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.shortcuts import render, render_to_response

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

def new_entry(request):
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
    data = serializers.serialize("python", Entries.objects.filter(pk = 1))
    moods = Entries.objects.filter(user_ID="kzhang").latest("submission_date")
    dates = Entries.objects.filter(user_ID = "kzhang").values('submission_date')
    context = {
        'form': form,
        'data': data,
        'moods': moods,
        'dates': dates,
    }
    return render(request, 'journal/new_entry.html', context)
def submitted(request): #OBSOLETE, used for testing
    # if 'request.user' in locals() or 'request.user' in globals()
    #     user_id = request.user
    # else
    # user_id = "courtland"
    user_id = request.user
    context = {
        'user_id': user_id,
    }
    template = loader.get_template('journal/get_entry/submitted.html')
    return HttpResponse(template.render(context,request))


def graph(request, id): #OBSOLETE, used for testing
    data = serializers.serialize("python",Entries.objects.filter(pk = id))
    moods = Entries.objects.get(pk=id)
    template = loader.get_template('journal/graph.html')
    context = {
        'moods': moods,
        'data': data,
    }
    return HttpResponse(template.render(context, request))

def get_entry(request):
    user_id = request.user
    q = Entries.objects.filter(user_ID=user_id)
    moods = q.latest('submission_date')
    form_txt = moods.entry_text
    dates = Entries.objects.filter(user_ID = user_id).values('submission_date')

    context = {
        'id': user_id,
        'moods': moods,
        'form_txt': form_txt,
        'dates': dates,
    }
    template = loader.get_template('journal/get_entry.html')
    return HttpResponse(template.render(context,request))
# def get_entry(request, id, date_str):
#     form = EntryForm()
#     set_date = datetime.strptime(date_str, "%m/%d/%Y")
#     print(set_date)
#     return HttpResponseRedirect(submitted(request))
#     #moods = Entries.objects.get(submission_date = )
