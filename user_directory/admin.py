from django.contrib import admin

from ads.models import Collection
from user_directory.models import Users, Location

admin.site.register(Location)
admin.site.register(Users)
admin.site.register(Collection)