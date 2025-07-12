from django.contrib import admin
from .models import massage, CountView, DoorClick
# Register your models here.

admin.site.register(massage)
admin.site.register(CountView)
admin.site.register(DoorClick)