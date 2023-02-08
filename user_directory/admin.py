from django.contrib import admin
from user_directory.models import Users, Location

admin.site.register(Location)
admin.site.register(Users)