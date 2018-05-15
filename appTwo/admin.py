from django.contrib import admin
from appTwo.models import User, EspTest, AccModel, GpsModel

# Register your models here.
admin.site.register(User)
admin.site.register(EspTest)
admin.site.register(AccModel)
admin.site.register(GpsModel)
