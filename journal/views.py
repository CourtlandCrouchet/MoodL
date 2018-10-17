from django.http import HttpResponse
from django.template import loader

from .models import Entries


def index(request):
    latest_entries_list = Entries.objects.order_by('-submission_date')[:5]
    template = loader.get_template('journal/index.html')
    context = {
        'latest_entries_list': latest_entries_list,
    }
    return HttpResponse(template.render(context, request))
