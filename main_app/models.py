from django.db import models


from django.db import models
from django.urls import reverse



class Property(models.Model):
    # define the columns, and the datatypes enforeced in each row
    location = models.CharField(max_length=100)
    price = models.IntegerField()  #models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    

    def get_absolute_url(self):
        
        return reverse('properties-detail', kwargs={'property_id': self.id})

    def __str__(self):
        return self.name

# all caps tells other python developers don't change this 
# variable (python convention)
APPOINTMENTSFORM = (
    ("R", "Rent"),
    ("S", "Sale"),
) 

# to define the many side after the one
class Appointment(models.Model):
    date = models.DateField()
    # select menu (Dropdown)
    appointment = models.CharField(
        max_length=1,
        choices=APPOINTMENTSFORM,
        default=APPOINTMENTSFORM[0][0] # B is the default value
    )

    # create a cat_id in psql on the feeding_table, django
    # automatically ads the _id
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

    def __str__(self):
        # self.get_<propertynamethathasthechoices>_display()
        return f"{self.get_appointment_display()} on {self.date}"

    class Meta:
        # lookup diffeappointment attributes from docs
        ordering = ['-date'] # newest feeding first when displayed