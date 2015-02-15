from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from models import Visa, VisaForm
from django.template import RequestContext

from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def homepage(request):
    if request.method == 'GET':
        form = VisaForm()
        return render_to_response('index.html', {'form':form },context_instance=RequestContext(request))

    if request.method == 'POST':
        # save sent data.. and send the "complete table"
        try:
            visa = Visa(name=request.POST.get('name',''),
                    passport=request.POST.get('passport', ''),
                    nationality=request.POST.get('nationality', ''),
                    dob=request.POST.get('dob', ''),
                    gender=request.POST.get('gender', ''),
                   )
            visa.save()
            objs = Visa.objects.all()
            response_str = '<table class="table table-striped"> '
            response_str+= '''<thead>
                                <tr>
                                 <th>Name</th>
                                 <th>Passport</th>
                                 <th>Date Of Birth</th>
                                 <th>Nationality</th>
                                 <th>Gender</th>
                              </thead><tbody>'''

            for obj in objs:
                response_str+='''<tr>
                                  <td>{name}</td>
                                  <td>{passport}</td>
                                  <td>{dob}</td>
                                  <td>{nationality}</td>
                                  <td>{gender}</td></tr>

                                  '''.format(name=obj.name,passport=obj.passport,
                                              dob=str(obj.dob), nationality=obj.nationality,gender=obj.gender
                                              )
            response_str+='</tbody></table>'


        except Exception as e: # This exception is also displayed in template.
            return HttpResponse('Error: ' + str(e))

        """
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
        response_str+=str(obj)
        """
        return HttpResponse(response_str)
