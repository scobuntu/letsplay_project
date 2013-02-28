from django import forms
from letsplay.models import AgeGroup, Category

class CustomiseForm(forms.Form):

	GENDERS=(
				('Gender', 'Gender'), 
				('Boy', 'Boy'), 
				('Girl', 'Girl'),
				('No Preference', 'No Preference'),
			)

	name = forms.CharField(max_length=100, initial="Name")
	gender = forms.ChoiceField(choices=GENDERS)
	education = forms.ModelChoiceField(queryset=AgeGroup.objects.all(), empty_label="Age")
	interests = forms.ModelChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Category.objects.all(), empty_label=None)

