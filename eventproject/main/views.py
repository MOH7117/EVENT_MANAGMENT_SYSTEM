from django.shortcuts import render, redirect
from datetime import date,time,datetime
from .models import Event , Venue
from django.http import HttpRequest,HttpResponseRedirect, HttpResponse


def home_page(request: HttpRequest):
    
    return render(request , 'main/base.html' , {'welcome':'Welcome To Our Events'})


def all_events(request: HttpRequest):
    event_list = Event.objects.all().order_by('event_date')
    return render(request , 'main/event_list.html' , {'event_list': event_list})

def add_venue(request: HttpRequest):
    if request.method == "POST":
        new_venue = Venue(
            name= request.POST["name"],
            addrise = request.POST["addrise"],
            phone = request.POST["phone"], 
            email_addriss=request.POST["email"],
            websit = request.POST["websit"])
        new_venue.save()

        return redirect("main:list-venues")
    return render(request, "main/add_venue.html")


def list_venues(request: HttpRequest):
    venue_list = Venue.objects.all().order_by('name')
    return render(request, 'main/venue.html',{"venue_list":venue_list})


def show_venue(request:HttpRequest, venue_id):
    veneu = Venue.objects.get(pk=venue_id)
    return render(request, 'main/show_venue.html',{"veneu":veneu})


def search_venues(request: HttpRequest):
    if request.method == "POST":
        searched = request.POST['searched']
        venues = Venue.objects.filter(name__contains=searched)

        return render(request, 'main/search_venues.html',{'searched':searched, 'venues':venues})
    else:
         return render(request, 'main/search_venues.html',{})


def update_venue(request: HttpRequest, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    if request.method == "POST":
        venue.name = request.POST["name"]
        venue.addrise = request.POST["address"]
        venue.phone = request.POST["phone"]
        venue.email_addriss = request.POST["email"]
        venue.websit = request.POST["website"]
        #to check if user chosen a file to upload for the update
        venue.save()
        return redirect("main:list-venues")
    return render(request, 'main/update_venue.html')



def update_event(request: HttpRequest, event_id):
    event = Event.objects.get(pk=event_id)
    if request.method == "POST":
        event.name = request.POST["name"]
        event.event_date = request.POST["date"]
        event.venue = request.POST["venue"]
        event.manager = request.user
        event.Description = request.POST["description"]
        #to check if user chosen a file to upload for the update
        event.save()
        return redirect("main:list-events")
    return render(request, 'main/update_event.html')

#Delete an Event
def delete_event(request:HttpRequest, event_id):
     event = Event.objects.get(pk=event_id) 
     event.delete()
     return redirect('main:list-events')


#Delete an Venue
def delete_venue(request:HttpRequest, venue_id):
     venue = Venue.objects.get(pk=venue_id) 
     venue.delete()
     return redirect('main:list-venues')



def add_event(request : HttpRequest):


    if request.method == "POST":
        #to add a new entry
        new_event = Event(
            name= request.POST["name"],
            event_date = request.POST["date"],
            venue = request.POST["venue"], 
            manager=request.user,
            Description = request.POST["description"])
        new_event.save()
        return redirect("main:list-events")


    return render(request, "main/add_event.html")