from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from models import Visa, VisaForm
from django.template import RequestContext

from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def homepage(request):
    if request.method == 'GET':
        form = VisaForm()
        return render_to_response('index.html', {'form':form},context_instance=RequestContext(request))

    if request.method == 'POST':
        form = VisaForm(request.POST)

        return HttpResponse(str(request.POST))
