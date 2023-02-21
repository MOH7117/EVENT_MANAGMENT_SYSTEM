from django.db import models
from django.contrib.auth.models import User

class venue(models.Model):
    name = models.CharField('venue name' , max_length=120)
    addrise = models.CharField('address ',max_length=120)
    zip_code =models.CharField('zip code' ,max_length=30)
    phone = models.CharField('phone' ,blank=True, max_length=20)
    email_addriss = models.EmailField('email' , blank=True, max_length=60)
    websit = models.URLField('web site' , blank=True , max_length=120)

    def __str__(self):
        return self.name



class myEventUser(models.Model):
    firstName= models.CharField(max_length=120)
    lastName = models.CharField(max_length=120)
    email = models.EmailField('email', max_length=120)

    def __str__(self):
        return self.firstName + ' ' +self.lastName

class event(models.Model):
    name = models.CharField('event name' , max_length=120)
    event_date = models.DateTimeField('event date' ,)
    # venue = models.CharField('venue' , max_length=120)
    venue = models.ForeignKey(venue , blank=True , null=True,on_delete=models.CASCADE)
    manager = models.ForeignKey(User , blank=True , null=True , on_delete=models.SET_NULL)
    Description = models.TextField(blank=True)
    attendess = models.ManyToManyField(myEventUser , blank=True)

    def __str__(self):
        return self.name

        


# Create your models here.
