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
	avatars = Avatar.objects.all()

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
	
	content_vars = {
	        'name': name,
	        'interests' : interests,
	        'games' : content.filter(content_type='Game'), 
	        'videos' : content.filter(content_type='Video'),
	        'avatars' : avatars.all(),
	        'backgrounds' : Background.objects.all()
	        }
	return render_to_response('customise.html', content_vars, RequestContext(request))

# Only allow a POST method to reach this page.
@require_http_methods(["POST"])
def play(request):
	
	name = request.session['name']
	choice_list = request.POST.getlist('choices')
	choices = Content.objects.filter(id__in=choice_list)

	content_vars = {
		'name' : name,
		'games' : choices.filter(content_type='Game'),
		'videos' : choices.filter(content_type='Video'),
		}
	
	return render_to_response('kids_page.html', content_vars, RequestContext(request))
	


	
