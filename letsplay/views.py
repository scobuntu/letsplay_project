# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.http import require_http_methods
from letsplay.forms import CustomiseForm
from letsplay.models import Category, AgeGroup, Content, Background, Avatar

def index(request):
	form = CustomiseForm()
	return render_to_response('index.html', {'form': form}, RequestContext(request))

# Only allow a POST method to reach this page.
@require_http_methods(["POST"])
def customise(request):
	name = request.POST['name']
	interests = request.POST.getlist('interest')
	age = request.POST.getlist('age-group')
	gender = request.POST.getlist('gender')
	form_vars = {'name': name, 'interests' : interests, 'age' : age, 'gender' : gender}
	#could create a user table that will save information
	#user = User(name= name, interests=interests, age=age, gender=gender)
	#user.save()
	Content.objects.filter(cateogry_contains='interests')
	return render_to_response('customise.html', form_vars, RequestContext(request))



	