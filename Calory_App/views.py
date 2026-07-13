from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.db.models import Sum
from .forms import *
from .models import *

# Create your views here.

def registerPage(req):
    if req.method == 'POST':
        form = RegisterForm(req.POST)

        if form.is_valid():
            form.save()
            # ProfileModel.objects.create(
            #     user = data
            # )
            messages.success(req,'User Created Successfully')
            return redirect('login')
    form = RegisterForm()
    context = {
        'form': form,
        'title': 'Register Form',
        'btn': 'Register',
        'a_t': 'Already Have an Account!',
        'a_b': 'Login Here'
    }
    return render(req,'pages/baseform.html',context)

def loginPage(req):
    if req.method == 'POST':
        form = AuthForm(req,req.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(req,user)
                messages.success(req,'Login Successfull')
                return redirect('dashboard')
            else:
                messages.error(req,'Wrong Credentials')
        else:
            messages.error(req,'Wrong Credentials')
        
    form = AuthForm()
    context = {
        'form': form,
        'title': 'Login Form',
        'btn': 'Login',
        'a_t': 'Don\'t Have an Account!',
        'a_b': 'Register Here'
    }
    return render(req,'pages/baseform.html',context)

@login_required
def profilePage(req):
    try:
        user = ProfileModel.objects.get(user = req.user)
    except ProfileModel.DoesNotExist:
        user = ProfileModel.objects.create(user = req.user)
    if req.method == 'POST':
        form = PProfileForm(req.POST,instance = user)
        if form.is_valid():
            data = form.save(commit=False)
            # if data.gender == 'Male':
            #     data.bmr = 66.47 + (13.75 * float(data.weight)) + (5.003 * float(data.height)) - (6.755 * float(data.age))
            # else:
            #     data.bmr = 655.1 + (9.563 * float(data.weight)) + (1.850 * float(data.height)) - (4.676 * float(data.age))
            data.save()
            messages.success(req,'Profile Updated Successfully')
            return redirect('dashboard')
    form = PProfileForm(instance = user)
    context = {
        'form': form,
        'title': 'Personal Information',
        'btn': 'Update Profile'
    }
    return render(req,'pages/baseform.html',context)
@login_required
def consumeCaloryPage(req):
    user = req.user
    if req.method == 'POST':
        form = CaloryConsumptionForm(req.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = user
            data.save()
            messages.success(req,'Calory Consumption Data Saved')
            return redirect('dashboard')
    form = CaloryConsumptionForm()
    context = {
        'form': form,
        'title': 'Daily Calory Consumption',
        'btn': 'Save'
    }
    return render(req,'pages/baseform.html',context)
@login_required
def dashboardPage(req):
    user = req.user
    allcaloryconsumed = CaloryConsumptionModel.objects.filter(user = req.user)
    try:
        profile = ProfileModel.objects.get(user = req.user)
        bmr = profile.bmr or 0
        calory_taken = CaloryConsumptionModel.objects.filter(user = user).aggregate(total=Sum('calory'))['total'] or 0
        remains = float(bmr) - float(calory_taken)
    except ProfileModel.DoesNotExist:
        bmr = 0
        calory_taken = 0
        remains = 0
    
    context = {
        'allcalcon': allcaloryconsumed,
        'bmr': bmr,
        'remains': remains,
        'calory_taken': calory_taken
    }
    return render(req,'pages/dashboard.html',context)

def logoutPage(req):
    logout(req)
    return redirect('login')
