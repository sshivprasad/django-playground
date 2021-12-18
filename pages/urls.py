from django.contrib import admin
from django.urls import path
from .views import DateView, PersonView


urlpatterns = [
    path('date', DateView.as_view(template_name='date.html'), name='date'),
    path('person', PersonView.as_view(template_name='person.html'), name='person'),
]
