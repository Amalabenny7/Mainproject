import smtplib

from django.shortcuts import render
from staff.models import StaffId
from login.models import Login
from django.core.files.storage import FileSystemStorage
from datetime import datetime
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.

def add_staff(request):
    if request.method=="POST":
        us = request.POST.get('un')
        ps = request.POST.get('pass')
        if Login.objects.filter(username=us,password=ps).exists():
            messages.error(request,"username and password already exists")
            # return mng_staff(request)
        else:
            obj = StaffId()
            obj.name=request.POST.get('n')
            obj.place=request.POST.get('place')
            obj.dob = request.POST.get('dob')
            obj.ph_no=request.POST.get('phno')
            obj.email=request.POST.get('email')
            obj.address=request.POST.get('address')
            myfile = request.FILES['photo']
            fs = FileSystemStorage()
            fs.save(myfile.name, myfile)
            obj.photo = myfile.name
            obj.username=request.POST.get('un')
            obj.password = request.POST.get('pass')
            obj.status='active'
            obj.save()

            ob = Login()
            ob.username = obj.email
            ob.password = obj.password
            ob.type = "staff"
            ob.u_id=obj.staff_id
            ob.save()

            email = "projectmailbg@gmail.com"

            em = obj.email
            pwd=obj.password

            sub = "staff added successfully"
            msg = 'Username:' + em + '& Password: ' + pwd
            text = f'subject :{sub}\n\n{msg}'
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(email, 'iqjjrhsyerovorav')
            server.sendmail(email, str(em), text)

            messages.success(request,"successfully registered")
            return HttpResponseRedirect('/staff/manage/')

    return render(request, 'staff/add_staff.html')




def mng_staff(request):
    # obj=StaffId.objects.all().order_by('-staff_id')
    # context={
    #     'a':obj
    # }
    if request.method == "POST":
        search_query = request.POST.get("bk", "").strip()

        staff = StaffId.objects.all().order_by('-staff_id')
        if search_query:
            # Try to match the search query to job name, location, or date
            staff = staff.filter(name__icontains=search_query) | staff.filter(status__icontains=search_query)

            # Check if the input is a valid date

            try:
                search_date = datetime.strptime(search_query, "%Y-%m-%d").date()
                staff = staff | StaffId.objects.filter(dob=search_date)  # Ensure your Job model has 'posted_date'
            except ValueError:
                pass  # If it's not a date, ignore this part

        return render(request, 'staff/manage staff.html', {"a": staff})
    else:
        uuh = StaffId.objects.all()
        context = {
            "a": uuh
        }

    return render(request, 'staff/manage staff.html',context)

def block(request,idd):
    obj=StaffId.objects.get(staff_id=idd)
    obj.status='blocked'
    obj.save()
    return mng_staff(request)

def edit(request,idd):
    obj = StaffId.objects.get(staff_id=idd)
    context = {
        'a': obj
    }
    if request.method=="POST":
        obj = StaffId.objects.get(staff_id=idd)
        obj.name=request.POST.get('n')
        obj.place=request.POST.get('place')
        obj.dob = request.POST.get('dob')
        obj.ph_no=request.POST.get('phno')
        obj.email=request.POST.get('email')
        obj.address=request.POST.get('address')
        myfile = request.FILES['photo']
        fs = FileSystemStorage()
        fs.save(myfile.name, myfile)
        obj.photo = myfile.name
        # obj.username=request.POST.get('un')
        obj.password = request.POST.get('pass')
        obj.save()
        return mng_staff(request)

    return render(request,'staff/edit_staff.html',context)

