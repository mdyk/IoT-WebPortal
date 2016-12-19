from django.shortcuts import render
from django.http import HttpResponse
from .models import Urzadzenie
from django.template import loader
from .forms import UrzadzenieForm
from django.http import HttpResponseRedirect



def index(request):
    template = loader.get_template('index.html')
    context = {
    'urzadzenia': Urzadzenie.objects.all(),
    }
    if request.POST:
        form=UrzadzenieForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('index')
    else:
        form = UrzadzenieForm()
    args = {}

    args['form'] = form
    return HttpResponse(template.render(context, request))

