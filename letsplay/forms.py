from django import forms
from letsplay.models import AgeGroup, Category

class CustomiseForm(forms.Form):

	SEX = (
		('Gender', 'Gender'),
		('N/A', 'N/A'),
		('Male', 'Male'),
		('Female','Female'),
		)


	name = forms.CharField(max_length=100, initial="Name")
	sex = forms.ChoiceField(choices=SEX)
	age = forms.ModelChoiceField(queryset=AgeGroup.objects.all(), empty_label="Age")
	interests = forms.ModelChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Category.objects.all(), empty_label=None)

