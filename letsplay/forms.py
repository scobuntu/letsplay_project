from django import forms
from letsplay.models import Category

class CustomiseForm(forms.Form):

	GENDERS=(
				('Gender', 'Gender'), 
				('Boy', 'Boy'), 
				('Girl', 'Girl'),
				('No Preference', 'No Preference'),
			)
	LEVEL=(
				('Education Level', 'Education Level'), 
				('Pre-School', 'Pre-School'),
				('Primary School', 'Primary School'),
				('No Preference', 'No Preference'), 
			)

	name = forms.CharField(max_length=100, initial="Name:")
	gender = forms.ChoiceField(choices=GENDERS)
	education = forms.ChoiceField(choices=LEVEL)
	interests = forms.ModelChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Category.objects.all(), empty_label=None)

