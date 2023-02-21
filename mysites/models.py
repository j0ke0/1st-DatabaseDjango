from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    MERRIED = 'Merried'
    SINGLE = 'Single'
    STATUS = [
        (SINGLE, 'single'),
        (MERRIED , 'married')
        ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    nickname = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=8, choices= STATUS, blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.first_name.title()} {self.user.last_name.title()} - Username: {self.user.username}"

class Plan(models.Model):

    plan_name = models.CharField(max_length=50)
        
    def __str__(self):
        return f"{self.plan_name.title()}"

class PlanDetails(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    detail = models.TextField(null=True, blank=True)
    sig_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.plan.plan_name.title()
    
    class Meta:
        unique_together = [['plan', 'detail']]

class Subscription(models.Model):
    expire_date = models.DateField()
    expire_hour = models.TimeField()
    users = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    plan_start_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.users.first_name.title()} {self.users.last_name.title()} - Plan type: {self.plan.plan_name}"

    class Meta:
        unique_together = [['users', 'plan']]

class Announcement(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    announcement = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title.title()}"
    