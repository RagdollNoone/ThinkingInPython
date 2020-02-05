from django.contrib import admin
from .models import Room, Group, User, Meet, Sign

# Register your models here.
admin.site.register(Room)
admin.site.register(Group)
admin.site.register(User)
admin.site.register(Meet)
admin.site.register(Sign)
