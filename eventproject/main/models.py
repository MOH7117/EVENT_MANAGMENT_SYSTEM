from django.db import models
from django.contrib.auth.models import User

class Venue(models.Model):
    name = models.CharField('venue name' , max_length=120)
    addrise = models.CharField('address ',max_length=120)
    phone = models.CharField('phone' ,blank=True, max_length=20)
    email_addriss = models.EmailField('email' , blank=True, max_length=60)
    websit = models.URLField('web site' , blank=True , max_length=120)
    venue_image = models.ImageField(null=True, blank=True, upload_to="images/")
    


    def __str__(self):
        return self.name



class EventUser(models.Model):
    firstName= models.CharField(max_length=120)
    lastName = models.CharField(max_length=120)
    email = models.EmailField('email', max_length=120)

    def __str__(self):
        return self.firstName + ' ' +self.lastName

class Event(models.Model):
    name = models.CharField('event name' , max_length=120)
    event_date = models.DateTimeField('event date' ,)
    # venue = models.CharField('venue' , max_length=120)
    venue = models.CharField('veune name' , max_length=120)    #--------------------edit venue to venue_location
    manager = models.ForeignKey(User , blank=True , null=True , on_delete=models.SET_NULL)
    Description = models.TextField(blank=True)
    event_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.name

class Review(models.Model):

    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    rating =  models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return f"{self.user} : {self.venue}"

class Review_Event(models.Model):

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    rating =  models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return f"{self.user} : {self.event}"


# Create your models here.
