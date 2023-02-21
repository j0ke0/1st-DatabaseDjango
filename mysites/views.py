from django.shortcuts import render, redirect
from .models import Subscription, Plan, Announcement, PlanDetails
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import EditFrom, PlanFrom, ProfileForm, AnnounceFrom, Detailsplan

def index(response):
    return render(response, 'mysites/index.html')

@login_required
def client(response):
    if response.user.is_superuser:
        profile = User.objects.all().order_by('is_active')
        context = {'profile': profile}
        return render(response, 'mysites/client.html', context)
    else:
        return redirect('mysites:index')
    
@login_required
def add_profile(response):
    if response.user.is_superuser:
        profile = ProfileForm()
        names = User.objects.all().order_by('first_name')
        if response.method == 'POST':
            profile = ProfileForm(response.POST)
            if profile.is_valid():
                profile.save()
                return redirect('mysites:entry')
        context = {'profile': profile, 'names': names}
        return render(response, 'mysites/add_profile.html', context)
    else:
        return redirect('mysites:index')

@login_required
def info(response):
    if response.user.is_superuser:
        form = Subscription.objects.all().order_by('expire_date')
        context = {'form': form}
        return render(response, 'mysites/info.html', context)
    else:
        return redirect('mysites:index')

@login_required
def entry(response):
    if response.user.is_superuser:
        form = EditFrom
        fork = User.objects.all().order_by('first_name')
        if response.method == 'POST':
            form = EditFrom(response.POST)
            if form.is_valid():
                form.save()
                return redirect('mysites:info')
        context = {'form': form, 'fork': fork }
        return render(response, 'mysites/entry.html', context)
    else:
        return redirect('mysites:index')

@login_required
def edit_info(response, pk):
    if response.user.is_superuser:
        customer = Subscription.objects.get(id=pk)
        form = EditFrom(instance=customer)
        if response.method == 'POST':
            form = EditFrom(response.POST, instance=customer)
            if form.is_valid():
                form.save()
                return redirect('mysites:info')
        context = {'form': form}    
        return render(response, 'mysites/entry.html', context)
    else:
        return redirect('mysites:index')

@login_required
def delete(response, pk):
    if response.user.is_superuser:
        customer = Subscription.objects.get(id=pk)
        if response.method == 'POST':
            customer.delete()
            return redirect('mysites:info')
        context = {'customer': customer}
        return render(response, 'mysites/delete.html', context)
    else:
        return redirect('mysites:index')

@login_required
def add_plan(response):
    if response.user.is_superuser:
        fork = PlanDetails.objects.all()
        plan = Plan.objects.all()
        form = PlanFrom()
        if response.method == 'POST':
            form = PlanFrom(response.POST)
            if form.is_valid():
                form.save()
                return redirect('mysites:add_plan')
        context = {'form': form, 'plan': plan, 'fork': fork}
        return render(response, 'mysites/add_plan.html', context)
    else:
        return redirect('mysites:index')

@login_required   
def open_plan_info(response):
    if response.user.is_superuser:
        form = Detailsplan()
        if response.method == 'POST':
            form = Detailsplan(response.POST)
            if form.is_valid():
                form.save()
                return redirect('mysites:add_plan')
        context = {'form': form}
        return render(response, 'mysites/open_plan_info.html', context)
    else:
        return render('mysites:index')
    
@login_required
def delete_plan_info(response, pk):
    if response.user.is_superuser:
        customer = PlanDetails.objects.get(id=pk)
        if response.method == 'POST':
            customer.delete()
            return redirect('mysites:add_plan')
        context = {'customer': customer}
        return render(response, 'mysites/delete_plan_info.html', context)
    else:
        return redirect('mysites:index')
      

@login_required
def edit_plan(response, pk):
    if response.user.is_superuser:
        editplan = Plan.objects.get(id=pk)
        e_plan = PlanFrom(instance=editplan)
        if response.method == 'POST':
            e_plan = PlanFrom(response.POST, instance=editplan)
            if e_plan.is_valid():
                e_plan.save()
                return redirect('mysites:add_plan')
        context = {'e_plan': e_plan}
        return render(response, 'mysites/plan_area.html', context)
    else:
        return redirect('mysites:index')

@login_required
def del_plan(response, pk):
    if response.user.is_superuser:
        del_plan = Plan.objects.get(id=pk)
        if response.method == 'POST':
            del_plan.delete()
            return redirect('mysites:add_plan')
        context = {'del_plan': del_plan}
        return render(response, 'mysites/del_area.html', context)
    else:
        return redirect('mysites:index')

@login_required
def announcement(response):
    if response.user.is_superuser:
        form = AnnounceFrom()
        visual = Announcement.objects.all().order_by('date_added')
        if response.method == 'POST':
            form = AnnounceFrom(response.POST)
            if form.is_valid():
                form.save()
                return redirect('mysites:announcement')
        context = {'form': form, 'visual': visual}
        return render(response, 'mysites/announcement.html', context)
    else:
        return redirect('mysites:index')

@login_required
def verify_del(response, pk):
    if response.user.is_superuser:
        files = Announcement.objects.get(id = pk)
        context = {'files': files}
        return render(response, 'mysites/del_announce.html', context)
    else:
        return redirect('mysites:index')

@login_required
def del_announce(response, pk):
    if response.user.is_superuser:
        delannouncement = Announcement.objects.get(id= pk)
        if response.method == 'POST':
            delannouncement.delete()
            return redirect('mysites:announcement')
        context = {'delannouncement': delannouncement}
        return render(response, 'mysites/del_announce.html', context)
    else:
        return redirect('mysites:index')

@login_required
def edit_announce(response, pk):
    if response.user.is_superuser:
        edit_form = Announcement.objects.get(id=pk)
        form = AnnounceFrom(instance=edit_form)
        if response.method == 'POST':
            form = AnnounceFrom(response.POST, instance=edit_form)
            if form.is_valid():
                form.save()
                return redirect('mysites:announcement')
        context = {'edit_form': edit_form, 'form': form}
        return render(response, 'mysites/edit_announce.html', context)
    else:
        return redirect('mysites:index')

@login_required
def customer_view(response):
    form = Announcement.objects.all()
    fork = Subscription.objects.filter(users=response.user)
    context = {'form': form, 'fork': fork}
    return render(response, 'mysites/customer_view.html', context)

@login_required
def portfolio(response, pk):
    form = Subscription.objects.filter(users_id = pk)
    fork = PlanDetails.objects.all() 
    context = {'form': form, 'fork': fork}
    return render(response, 'mysites/portfolio.html', context)
