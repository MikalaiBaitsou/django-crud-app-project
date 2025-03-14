from django import forms
from .models import Appointment
from .models import Property

class AppointmentForm(forms.ModelForm):
    # meta configuration variable for your class
    # this is just the way django has defined it
    class Meta:
        model = Appointment
        fields = ['date', 'appointment']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            )
        }

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['location', 'price', 'description', 'image']