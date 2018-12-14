# Register your models here.
from django.contrib import admin

from .models import Message, StatusUpdate, UserProfile

# from __future__ import unicode_literals


admin.site.register(UserProfile)
admin.site.register(StatusUpdate)
admin.site.register(Message)
