from django.urls import path
from .import views

app_name="main"

urlpatterns = [
    path('' , views.home_page , name='home_page'),
    path('events/' , views.all_events , name='list-events'),
    path('add_venue' , views.add_venue , name='add_venue'),
    path('list_venues' , views.list_venues , name='list-venues'),
    path('show_venue/<venue_id>' , views.show_venue , name='show-venue'),
    path('show_event/<event_id>' , views.show_event , name='show-event'),
    path('update_venue/<venue_id>' , views.update_venue , name='update-venue'),
    path('update_event/<event_id>' , views.update_event , name='update-event'),
    path('add_event' , views.add_event , name='add-event'),
    path('delete_event/<event_id>' , views.delete_event , name='delete-event'),
    path('delete_venue/<venue_id>' , views.delete_venue , name='delete-venue'),
    path("review/venue/add/<venue_id>/", views.add_review, name="add_review"),
    path("review/event/add/<event_id>/", views.add_review_evevnt, name="add_review_event"),
]