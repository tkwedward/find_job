#coding:utf-8#-*-

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm, FreelanceForm
from .models import Job_detail
from django.contrib.auth.models import User
# 製造頁面

    # 第一頁
def get_name(request):
    form = ContactForm()
    user = request.user
    return render(request, 'name.html', {'form': form, 'type':'normal', 'user':user})

def get_name_2(request):
    form = FreelanceForm()
    return render(request, 'name.html', {'form': form, 'type2':'freelance'})

    #第二頁
def job_list(request):#2.1
    model = Job_detail.objects.order_by('-date')
    return render(request, 'list_view.html', {'list':model})

def job_list_work_time(request):#2.2
    model = Job_detail.objects.order_by('working_hour')
    return render(request, 'list_view.html', {'list':model})

def job_list_salary(request):#2.3
    return render(request, 'name.html', {'form': form})

def Freelance_add(request):
    if request.method == "POST":
        form = FreelanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = FreelanceForm()
    return render(request, 'freelance_form.html', {'form': form})

#功能

def added(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'name.html', {'form': form})


def search(request):
    keyword = request.GET['user_name']
    result = Job_detail.objects.all().filter(company__icontains=keyword)
    return render(request, 'job_search.html', locals())
    # return HttpResponse(keyword)

def customer_order(request):
    keyword = request.GET['orders']
    if keyword == "working_hr_descending":
        result = Job_detail.objects.all().order_by('-working_hour')
    elif keyword == "working_hr_ascending":
        result = Job_detail.objects.all().order_by("working_hour")
    elif keyword == "salary_descending":
        result = Job_detail.objects.all().order_by("-salary")
    elif keyword == "salary_ascending":
        result = Job_detail.objects.all().order_by("salary")

    elif keyword == "time_descending":
        result = Job_detail.objects.all().order_by("date")

    elif keyword == "time_ascending":
        result = Job_detail.objects.all().order_by("-date")

    return render(request, 'list_view.html', {'list':result})
    # return HttpResponse(keyword)


def example(request):
    return HttpResponse("success<br><a href='/job/form'>back home </a>")
