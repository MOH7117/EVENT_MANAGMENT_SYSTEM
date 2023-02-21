from django.contrib import admin
from .models import venue , event , myEventUser

# admin.site.register(venue)
admin.site.register(myEventUser)
# admin.site.register(event)

# Register your models here.

@admin.register(venue)
class venueAdmin(admin.ModelAdmin):
    list_display = ('name' , 'addrise' , 'zip_code' )
    ordering = ('name',)
    search_fields = ('name' , 'addrise')

@admin.register(event)
class eventAdmin(admin.ModelAdmin):
    list_display = ('name' ,'event_date'  )
    fields =(('name' , 'event_date' , 'venue') ,  ('Description') , ('attendess'), 'manager')
    ordering = ('event_date',)
    list_filter = ('event_date' , 'venue')    