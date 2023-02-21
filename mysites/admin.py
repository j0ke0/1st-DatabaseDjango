from django.contrib import admin
from .models import Profile, Plan, Subscription, Announcement, PlanDetails

admin.site.register(Profile)
admin.site.register(Plan)
admin.site.register(Subscription)
admin.site.register(Announcement)
admin.site.register(PlanDetails)