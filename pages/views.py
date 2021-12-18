from django.shortcuts import render
from django.views.generic import FormView, CreateView
from .forms import DateForm, PersonForm
# Create your views here.


class DateView(FormView):
    form_class = DateForm


class PersonView(FormView):
    form_class = PersonForm


