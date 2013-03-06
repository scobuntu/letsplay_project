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
	request.session['name'] = name
	
	interests = request.POST.getlist('interests')
	age = request.POST.get('age')
	gender = request.POST.get('sex')
	
	content = Content.objects.all()

	if age == '5' or age == '':
		content = content.all()
	else:
		content = content.filter(ageGroup=age)
	
	if gender == 'Male' or gender=='Female':
		content = content.filter(sex=gender)
	else:
		content = content.all()

	if len(interests) == len(Category.objects.all()) or interests == []:
		content = content.all()
	else:
		content = content.filter(category__pk__in=interests)
	
	form_vars = {
	        'name': name,
	        'interests' : interests,
	        'games' : content.filter(content_type='Game'), 
	        'videos' : content.filter(content_type='Video'), 
	        'gender' : gender,
	        'age' : age
	        }
	return render_to_response('customise.html', form_vars, RequestContext(request))

# Only allow a POST method to reach this page.
@require_http_methods(["POST"])
def play(request):
	
	name = request.session['name']
	choice_list = []
	choices = request.POST.getlist('choices')
	
	return render_to_response('kids_page.html', {'choices' : choices, 'name' : name}, RequestContext(request))
	


	
