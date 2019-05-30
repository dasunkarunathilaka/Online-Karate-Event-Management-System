# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import *

# These tables are shown in 'http://127.0.0.1:8000/admin/' only if they are registered.

admin.site.register(Association)
admin.site.register(Slkf)
admin.site.register(Province)
admin.site.register(District)
admin.site.register(Player)
admin.site.register(Coach)
admin.site.register(Event)
admin.site.register(User)

