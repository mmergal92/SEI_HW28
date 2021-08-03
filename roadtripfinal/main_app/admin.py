from django.contrib import admin
from main_app.models import Stays, User, Roadtripping, Roadtrips, Lodging, PlanningLodging

# Register your models here.
admin.site.register(Stays)
admin.site.register(User)
admin.site.register(Roadtrips)
admin.site.register(Roadtripping)
admin.site.register(Lodging)
admin.site.register(PlanningLodging)