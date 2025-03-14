from django.urls import path
# import all the functions in views file
# as methods on a views object
from . import views

urlpatterns = [
    # localhost:8000, 
    # in the views folder we have home function
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('properties/', views.property_index, name='properties-index'),
    # property_id is the name of our param
    path('properties/<int:property_id>/', views.property_detail, name='properties-detail'),
    # allow render CBV's as_view()
    path('properties/create/', views.PropertyCreate.as_view(), name='property-create'),
    # CBV expect the params name to be pk (primary key)
    path('properties/<int:pk>/update/', views.PropertyUpdate.as_view(), name='property-update'),
    path('properties/<int:pk>/delete/', views.PropertyDelete.as_view(), name='property-delete'),
    # 1 to many creation of a appointment (handling the post request from the appointment form)
    path('properties/<int:property_id>/add_appointment/', views.add_appointment, name='add-appointment'),
    # New URL for deleting an appointment
    path('properties/<int:property_id>/appointments/<int:pk>/delete/', views.AppointmentDelete.as_view(), name='appointment-delete'),
    path('accounts/signup', views.signup, name='signup'),
     
]