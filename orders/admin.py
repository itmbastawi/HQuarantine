from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(item_type)
admin.site.register(service_table)
admin.site.register(item_action)
admin.site.register(user_profile)
