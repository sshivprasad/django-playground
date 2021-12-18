from django import forms
from .models import Person


class DateInput(forms.DateInput):
    input_type = 'date'


class DateForm(forms.Form):
    date = forms.DateField(widget=DateInput)


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'dob', 'occupation')
        widgets = {'dob': DateInput()}
