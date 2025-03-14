from django.shortcuts import render, reverse

from django.contrib.auth.views import LoginView


from django.shortcuts import render, redirect


from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.http import HttpResponse

from .models import Property, Appointment

from .forms import AppointmentForm, PropertyForm

## AUTHORIZATION
from django.contrib.auth.decorators import login_required # function based views
from django.contrib.auth.mixins import LoginRequiredMixin # for CBVS

### Imports for the signup!
from django.contrib.auth import login # login function
from django.contrib.auth.forms import UserCreationForm # form instance for creating user



def signup(request):
    # view functions can handle multiple http requests
    error_message = ''
    # handle the post request (submission of the form)
    if request.method == "POST":
        # create a user form object that includes the data from the submitted form
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # save the form and create the user 
            # adds a row to the user table
            user = form.save()
            # login in the user 
            login(request, user)
            # this creates the request.user ^ in all our view functions

            return redirect('properties-index') # cats-index is the name of a path in urls.py
        else: 
            error_message = "Invalid sign up - try again"
    # handling the get request 
    form = UserCreationForm()
    return render(request, 'signup.html', {'form': form, 'error_message': error_message})




class PropertyUpdate(UpdateView):
    model = Property

    form_class = PropertyForm

    def form_valid(self, form):
        print(f"Form data: {form.cleaned_data}")  # Debug the submitted data
        return super().form_valid(form)
    
    # fields = ['location', 'price', 'description']
    

class PropertyDelete(DeleteView):
    model = Property
    success_url = '/properties/' 


class PropertyCreate(CreateView):
    
    model = Property

    form_class = PropertyForm

    def form_valid(self, form):
        print(f"Form data: {form.cleaned_data}")  # Debug the submitted data
        return super().form_valid(form)
    
    # fields = '__all__' # include all the keys on the Property model in the form


class AppointmentDelete(DeleteView):
    model = Appointment
    template_name = 'properties/appointment_confirm_delete.html'  # Custom template for confirmation

    def get_success_url(self):
        # Redirect back to the property detail page after deletion
        property_id = self.kwargs['property_id']
        return reverse('properties-detail', kwargs={'property_id': property_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['property_id'] = self.kwargs['property_id']
        return context


@login_required
def property_detail(request, property_id):

    property = Property.objects.get(id=property_id)
    print(f"Property ID: {property.id}, Price: {property.price}")  # Debug print
    appointment_form = AppointmentForm()# creates an instance of form

    
    return render(request, 'properties/detail.html', {'property': property, 'appointment_form': appointment_form})
    

@login_required
def add_appointment(request, property_id):
    
    form = AppointmentForm(request.POST)
    
    if form.is_valid():
        
        new_appointment = form.save(commit=False)
        
        new_appointment.property_id = property_id
        
        new_appointment.save()

   
    return redirect('properties-detail', property_id=property_id)




def property_index(request):
    
    properties = Property.objects.all()

    return render(request, 'properties/index.html', {'properties': properties})

class Home(LoginView):
    # specify a template
    template_name = 'home.html'


def about(request):
    # django knows to look for about.html
    # in a templates folder in our app
    return render(request, 'about.html')

