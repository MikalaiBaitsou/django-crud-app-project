from django.shortcuts import render, reverse


from django.shortcuts import render, redirect


from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.http import HttpResponse

from .models import Property, Appointment

from .forms import AppointmentForm, PropertyForm


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



def property_detail(request, property_id):

    property = Property.objects.get(id=property_id)
    print(f"Property ID: {property.id}, Price: {property.price}")  # Debug print
    appointment_form = AppointmentForm()# creates an instance of form

    
    return render(request, 'properties/detail.html', {'property': property, 'appointment_form': appointment_form})
    


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

def home(request):

    # HttpResponse is like res.send in Express
    return render(request, 'home.html')


def about(request):
    # django knows to look for about.html
    # in a templates folder in our app
    return render(request, 'about.html')

