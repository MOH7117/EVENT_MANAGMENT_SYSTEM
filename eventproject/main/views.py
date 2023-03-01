from django.shortcuts import render, redirect
from datetime import date,time,datetime
from .models import Event , Venue, Review, Review_Event
from django.http import HttpRequest,HttpResponseRedirect, HttpResponse


def home_page(request: HttpRequest):
    
    return render(request , 'main/base.html')


def all_events(request: HttpRequest):
    event_list = Event.objects.all().order_by('event_date')
    return render(request , 'main/event_list.html' , {'event_list': event_list})

def add_venue(request: HttpRequest):
    if request.user.is_staff:
        if request.method == "POST":
            new_venue = Venue(
                name= request.POST["name"],
                addrise = request.POST["addrise"],
                phone = request.POST["phone"], 
                email_addriss=request.POST["email"],
                websit = request.POST["websit"],
                venue_image = request.FILES["venue_image"])
            new_venue.save()
            return redirect('main:home_page')

        return render(request , "main/add_venue.html")
    return redirect('account:login')


def list_venues(request: HttpRequest):
    
        venue_list = Venue.objects.all().order_by('name')
        return render(request, 'main/venue.html',{"venue_list":venue_list})






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
        # event.manager = request.POST["mohammed"]
        event.manager = request.user
        event.Description = request.POST["description"]

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
            manager = request.user,
            Description = request.POST["description"],
            event_image = request.FILES["event_image"])
            
        new_event.save()
        return redirect("main:list-events")


    return render(request, "main/add_event.html")




def show_venue(request:HttpRequest, venue_id):
    if request.user.is_authenticated:
        venues = Venue.objects.get(pk=venue_id)
        reviews = Review.objects.filter(venue=venues)
        return render(request, 'main/show_venue.html',{"venue":venues,"reviews":reviews})
    return redirect('account:login')    


def show_event(request : HttpRequest, event_id):
    events = Event.objects.get(pk=event_id)
    reviews = Review_Event.objects.filter(event=events)
    return render(request, 'main/show_event.html',{"event":events,"reviews":reviews})



def add_review(request : HttpRequest, venue_id):

    if request.method == "POST":
        venue = Venue.objects.get(id=venue_id)
        new_review = Review(user = request.user, venue=venue, content = request.POST["content"], rating = request.POST["rating"])
        new_review.save()

    return redirect("main:show-venue", venue_id=venue_id)


def add_review_evevnt(request : HttpRequest, event_id):

    if request.method == "POST":
        events = Event.objects.get(id=event_id)
        new_review = Review_Event(user = request.user, event=events, content = request.POST["content"], rating = request.POST["rating"])
        new_review.save()
    return redirect("main:show-event", event_id=event_id)

   