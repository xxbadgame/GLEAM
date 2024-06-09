from django.contrib import admin
from .models import Mission, Task, Waitlist, Review, Payment, ApplyMission, Waitlist


# Register your models here.
admin.site.register(Mission)
admin.site.register(ApplyMission)
admin.site.register(Task)
admin.site.register(Waitlist)
admin.site.register(Review)
admin.site.register(Payment)