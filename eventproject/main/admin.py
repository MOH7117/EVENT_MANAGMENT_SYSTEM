from django.contrib import admin
from .models import Venue , Event , EventUser, Review, Review_Event

admin.site.register(Venue)
admin.site.register(EventUser)
admin.site.register(Event)
admin.site.register(Review)
admin.site.register(Review_Event)

# Register your models here.

 

