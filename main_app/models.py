from django.db import models

from django.urls import reverse
from django.contrib.auth.models import User



class Property(models.Model):
    # define the columns, and the datatypes enforeced in each row
    location = models.CharField(max_length=100)
    price = models.IntegerField()  #models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    image = models.ImageField(upload_to='properties/', null=True, blank=True)  # New image field
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def get_absolute_url(self):
        
        
        return reverse('properties-detail', kwargs={'property_id': self.id})
    

    def get_absolute_url(self):
        
        return reverse('properties-detail', kwargs={'property_id': self.id})

    def __str__(self):
        return self.location

# all caps tells other python developers don't change this 
# variable (python convention)
APPOINTMENTSFORM = (
    ("09:00", "9:00 AM - 10:00 AM"),
    ("10:00", "10:00 AM - 11:00 AM"),
    ("11:00", "11:00 AM - 12:00 PM"),
    ("12:00", "12:00 PM - 1:00 PM"),
    ("01:00", "1:00 PM - 2:00 PM"),
    ("02:00", "2:00 PM - 3:00 PM"),
    ("03:00", "3:00 PM - 4:00 PM"),
    ("04:00", "4:00 PM - 5:00 PM"),
    ("05:00", "5:00 PM - 6:00 PM"),
    ("06:00", "6:00 PM - 7:00 PM"),
) 

# to define the many side after the one
class Appointment(models.Model):
    date = models.DateField()
    # select menu (Dropdown)
    appointment = models.CharField(
        max_length=20,
        choices=APPOINTMENTSFORM,
        default=APPOINTMENTSFORM[0][0] # B is the default value
    )

    # create a property_id in psql on the feeding_table, django
    # automatically ads the _id
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

    def __str__(self):
        # self.get_<propertynamethathasthechoices>_display()
        return f"{self.get_appointment_display()} on {self.date}"

    class Meta:
        # lookup diffeappointment attributes from docs
        ordering = ['-date'] # newest feeding first when displayed