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
	age = request.POST['age']
	sex = request.POST['sex']
	interests = request.POST.getlist('interests')
	games = Content.objects.filter(content_type='Game', category__pk__in=interests, ageGroup__pk=age, sex=sex)
	form_vars = {'name': name, 'games' : games}
	#could create a user table that will save information
	#user = User(name= name, interests=interests, age=age, gender=gender)
	#user.save()
	return render_to_response('customise.html', form_vars, RequestContext(request))



	