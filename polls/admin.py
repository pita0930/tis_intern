from django.contrib import admin

from .models import User
from .models import Event

admin.site.register(User)
admin.site.register(Event)


# Register your models here.
