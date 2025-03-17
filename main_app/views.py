from django.shortcuts import render, redirect, reverse
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Property, Appointment
from .forms import AppointmentForm, PropertyForm
from django.contrib.auth.decorators import login_required  # Already imported
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.utils.decorators import method_decorator  # Add this import

def signup(request):
    error_message = ''
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('properties-index')
        else:
            error_message = "Invalid sign up - try again"
    form = UserCreationForm()
    return render(request, 'signup.html', {'form': form, 'error_message': error_message})

class PropertyUpdate(UpdateView):
    model = Property
    form_class = PropertyForm
    def form_valid(self, form):
        print(f"Form data: {form.cleaned_data}")
        return super().form_valid(form)

class PropertyDelete(DeleteView):
    model = Property
    success_url = '/properties/'

@method_decorator(login_required, name='dispatch')
class PropertyCreate(CreateView):
    model = Property
    form_class = PropertyForm
    template_name = 'main_app/property_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        print(f"Form data with user: {form.cleaned_data}, User: {self.request.user}")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('properties-index')

class AppointmentDelete(DeleteView):
    model = Appointment
    template_name = 'properties/appointment_confirm_delete.html'

    def get_success_url(self):
        property_id = self.kwargs['property_id']
        return reverse('properties-detail', kwargs={'property_id': property_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['property_id'] = self.kwargs['property_id']
        return context

@login_required
def property_detail(request, property_id):
    property = Property.objects.get(id=property_id)
    print(f"Property ID: {property.id}, Price: {property.price}")
    appointment_form = AppointmentForm()
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
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')