from django.shortcuts import render, redirect
from datetime import date,time,datetime
from .models import event, venue
from .forms import VenueForm, EventForm 
from django.http import HttpRequest,HttpResponseRedirect, HttpResponse


def home_page(request):
    
    return render(request , 'main/base.html' , {'welcome':'Welcome To Our Events'})


def all_events(request):
    event_list = event.objects.all().order_by('event_date')
    return render(request , 'main/event_list.html' , {'event_list': event_list})

def add_venue(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:        
        add_venue_form = VenueForm(request.GET)
        if submitted in request.GET:
            submitted = True
    return render(request ,'main/add_venue.html',{'form':add_venue_form , "submitted":submitted} )


def list_venues(request):
    venue_list = venue.objects.all().order_by('name')
    return render(request, 'main/venue.html',{"venue_list":venue_list})


def show_venue(request, venue_id):
    veneu_sh = venue.objects.get(pk=venue_id)
    return render(request, 'main/show_venue.html',{"veneu_sh":veneu_sh})


def search_venues(request):
    if request.method == "POST":
        searched = request.POST['searched']
        venues = venue.objects.filter(name__contains=searched)

        return render(request, 'main/search_venues.html',{'searched':searched, 'venues':venues})
    else:
         return render(request, 'main/search_venues.html',{})


def update_venue(request, venue_id):
     veneu_sh = venue.objects.get(pk=venue_id)
     form = VenueForm(request.POST or None, instance=veneu_sh)
     if form.is_valid():
            form.save()
            return redirect('list-venues')

     return render(request, 'main/update_venue.html',{"veneu_sh":veneu_sh, 'form':form})


def add_event(request):
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:        
        form = EventForm(request.GET)
        if submitted in request.GET:
            submitted = True
    return render(request ,'main/add_event.html',{'form':form , "submitted":submitted})


def update_event(request, event_id):
     Event = event.objects.get(pk=event_id)
     form = EventForm(request.POST or None, instance=Event)
     if form.is_valid():
            form.save()
            return redirect('list-events')

     return render(request, 'main/update_event.html',{"Event":Event, 'form':form})

#Delete an Event
def delete_event(request, event_id):
     Event = event.objects.get(pk=event_id) 
     Event.delete()
     return redirect('list-events')


#Delete an Venue
def delete_venue(request, venue_id):
     Venue = venue.objects.get(pk=venue_id) 
     Venue.delete()
     return redirect('list-venues')

