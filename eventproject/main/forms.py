from django import forms
from django.forms import ModelForm
from .models import venue, event



#create a venue form

class EventForm(ModelForm):
    class Meta:
        model = event
        fields = ('name' , 'event_date' , 'venue' , 'manager' ,'attendess', 'Description')
        labels = {
            'name' : '',
            'event_date' : '',
            'venue' : 'Venue',
            'manager' : 'Maneger',
            'attendess' : 'Attendees',
            'Description' : '',
        }
        widgets= {
            'name':forms.TextInput(attrs={'class':'form-control' , 'placeholder':'Event Name'}),
            'event_date':forms.TextInput(attrs={'class':'form-control' , 'placeholder':'Event Date'}),
            'venue':forms.Select(attrs={'class':'form-select','placeholder':'Venue'}),
            'manager':forms.Select(attrs={'class':'form-select' , 'placeholder':'Manager'}),
            'attendess':forms.SelectMultiple(attrs={'class':'form-control' , 'placeholder':'Attendess'}),
            'Description':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),

        }

#create a venue form


class VenueForm(ModelForm):
    class Meta:
        model = venue
        fields = ('name' , 'addrise' , 'zip_code' , 'phone' , 'email_addriss','websit')
        labels = {
            'name' : '',
            'addrise' : '',
            'zip_code' : '',
            'phone' : '',
            'email_addriss' : '',
            'websit' : '',
        }
        widgets= {
            'name':forms.TextInput(attrs={'class':'form-control' , 'placeholder':'please enter the name of venue'}),
            'addrise':forms.TextInput(attrs={'class':'form-control' , 'placeholder':'address of the venue'}),
            'zip_code':forms.TextInput(attrs={'class':'form-control','placeholder':'zip code'}),
            'phone':forms.TextInput(attrs={'class':'form-control' , 'placeholder':'phone number'}),
            'email_addriss':forms.EmailInput (attrs={'class':'form-control', 'placeholder':'email your'}),
            'websit':forms.TextInput(attrs={'class':'form-control' , 'placeholder':'website'})

        }

