from django.forms import ModelForm
from .models import Subscription, Plan, Profile, Announcement, PlanDetails
from django import forms

class EditFrom(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ('expire_date', 'expire_hour', 'plan', 'users', 'remarks')
        widgets = {
            'expire_date': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'YYYY-MM-DD',}),
            'expire_hour': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'HH:MM:SS'}),
            'plan': forms.Select(attrs={'class':'form-control'}),
            'users': forms.Select(attrs={'class':'form-control'}),
            'remarks': forms.Textarea(attrs={'class':'form-control'}),
        }

class PlanFrom(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ('plan_name',)
        widgets = {
            'plan_name': forms.TextInput(attrs={'class':'form-control'}),
        }
        

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user', 'nickname', 'phone', 'age', 'status')
        widgets = {
            'user': forms.Select(attrs={'class':'form-control'}),
            'nickname': forms.TextInput(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Mobile number'}),
            'age': forms.TextInput(attrs={'class':'form-control'}),
            'status': forms.Select(attrs={'class':'form-control'}),
        }

class AnnounceFrom(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ('title', 'announcement')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'announcement': forms.Textarea(attrs={'class':'form-control'}),
        }

class Detailsplan(forms.ModelForm):
    class Meta:
        model = PlanDetails
        fields = ('plan', 'detail')
        widgets = {
            'plan': forms.Select(attrs={'class':'form-control'}),
            'detail': forms.Textarea(attrs={'class':'form-control'}),
        }
        


