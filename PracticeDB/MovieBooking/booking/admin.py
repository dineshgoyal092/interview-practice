from django.contrib import admin

# Register your models here.
from .models import Movie, ExtendedUser, Theater, Screen, Seat, City, Show


admin.site.register(Movie)
admin.site.register(ExtendedUser)
admin.site.register(Theater)
admin.site.register(Screen)
admin.site.register(Seat)
admin.site.register(City)
admin.site.register(Show)