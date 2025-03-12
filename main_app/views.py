from django.shortcuts import render


from django.shortcuts import render, redirect


from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.http import HttpResponse

from .models import Property

from .forms import AppointmentForm


class PropertyUpdate(UpdateView):
    model = Property
    
    fields = ['location', 'price', 'description']
    

class PropertyDelete(DeleteView):
    model = Property
    success_url = '/properties/' 


class PropertyCreate(CreateView):
    
    model = Property
    
    fields = '__all__' # include all the keys on the Property model in the form
    



def property_detail(request, property_id):

    property = Property.objects.get(id=property_id)
    appointment_form = AppointmentForm()# creates an instance of form

    
    return render(request, 'properties/detail.html', {'Property': property, 'appointment_form': appointment_form})
    


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

