from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from models import Visa, VisaForm
from django.template import RequestContext

from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def homepage(request):
    if request.method == 'GET':
        form = VisaForm()
        return render_to_response('index.html', {'form':form},context_instance=RequestContext(request))

    if request.method == 'POST':
        # save sent data.. and send the "complete table"
        obj = VisaForm.objects.all()
        # generate an html table from obj
        response_str = '<table class="table table-striped"> '
        response_str+= '''<thead>
                            <tr>
                             <th>Name</th>
                             <th>Passport</th>
                             <th>Date Of Birth</th>
                             <th>Nationality</th>
                             <th>Gender</th>
                          </thead>'''
        return HttpResponse(response_str)
