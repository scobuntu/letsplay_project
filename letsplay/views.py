# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.http import require_http_methods

def index(request):
	return render_to_response('index.html', RequestContext(request))

# Only allow a POST method to reach this page.
@require_http_methods(["POST"])
def customise(request):
	name = request.POST['name']
	interests = request.POST.getlist('interest')
	age = request.POST.getlist('age-group')
	gender = request.POST.getlist('gender')
	form_vars = {'name': name, 'interests' : interests, 'age' : age, 'gender' : gender}
	return render_to_response('customise.html', form_vars, RequestContext(request))



	