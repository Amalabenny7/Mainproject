from django.shortcuts import render
from job.models import JobId,Application
from datetime import datetime
from django.http import HttpResponse
from job.serializers import android_seriliser1
from staff.models import StaffId
# import datetime
def add_job(request):
    ab=StaffId.objects.all()
    # print(datetime.today())
    curr_date = datetime.today().date()
    print(curr_date)
    context={
        'dt':curr_date,
        'sf':ab
    }

    if request.method=="POST":

        obj = JobId()
        obj.jobtitle=request.POST.get('n')
        obj.description=request.POST.get('des')
        obj.type=request.POST.get('type')
        obj.qualification=request.POST.get('quali')
        obj.location=request.POST.get('loc')
        obj.gender=request.POST.get('gender')
        obj.age=request.POST.get('age')
        obj.experience=request.POST.get('ex')
        obj.number_of_vacancy=request.POST.get('vacancy')
        obj.working_time=request.POST.get('time')
        obj.salary=request.POST.get('Salary')
        obj.last_date=request.POST.get('date')
        obj.c_name=request.POST.get('company_name')
        obj.c_details=request.POST.get('cdet')
        obj.statusl="accepted"
        obj.staff_id=request.POST.get('staff')
        obj.save()

        return manage(request)
    return render(request,'job/add_job.html',context)


def edit(request,idd):
    obj = JobId.objects.get(job_id=idd)
    context = {
        'r': obj
    }
    if request.method=="POST":
        obj = JobId.objects.get(job_id=idd)
        obj.jobtitle=request.POST.get('n')
        obj.description=request.POST.get('des')
        obj.type=request.POST.get('type')
        obj.qualification=request.POST.get('quali')
        obj.location=request.POST.get('loc')
        obj.gender=request.POST.get('gender')
        obj.age=request.POST.get('age')
        obj.experience=request.POST.get('ex')
        obj.vacancy=request.POST.get('vacancy')
        obj.working_time=request.POST.get('time')
        obj.salary=request.POST.get('Salary')
        obj.last_date=request.POST.get('date')
        obj.c_name=request.POST.get('company name')
        obj.c_details=request.POST.get('cdet')
        obj.statusl="accepted"
        obj.save()
        return manage(request)
    return render(request,'job/Update_job.html',context)

def delete(request,idd):
    obj=JobId.objects.get(job_id=idd)
    obj.statusl="blocked"
    obj.save()
    return manage(request)

def view(request):
    ss=request.session["u_id"]
    obj = JobId.objects.filter(staff_id=ss)
    context = {
        'oo': obj
    }
    return render(request,'job/view_job.html',context)

def view_job_new(request):
    obj = JobId.objects.all()
    context = {
        'oo': obj
    }
    return render(request,'job/view_jobnew.html',context)

def manage(request):
    if request.method == "POST":
        search_query = request.POST.get("bk", "").strip()

        jobs = JobId.objects.all().order_by('-job_id')
        if search_query:
            # Try to match the search query to job name, location, or date
            jobs = jobs.filter(jobtitle__icontains=search_query) | jobs.filter(location__icontains=search_query)

            # Check if the input is a valid date

            try:
                search_date = datetime.strptime(search_query, "%Y-%m-%d").date()
                jobs = jobs | JobId.objects.filter(last_date=search_date)  # Ensure your Job model has 'posted_date'
            except ValueError:
                pass  # If it's not a date, ignore this part

        return render(request, "job/manage_job.html", {"jobs": jobs})
    else:
        uuh=JobId.objects.all()
        context={
            "jobs":uuh
        }

    # obj=JobId.objects.all().order_by('-job_id')
    # context={
    #     'kk':obj
    # }
    return render(request,'job/manage_job.html',context)

from rest_framework.views import APIView,Response
from job.serializers import android_seriliser




class vwwww(APIView):
    def get(self,request):
        ob=JobId.objects.all()
        ser=android_seriliser(ob,many=True)
        return Response(ser.data)


def view_job_details(request,idd):
    obj = JobId.objects.get(job_id=idd)
    context = {
        'oo': obj
    }
    return render(request,'job/job-detail.html',context)

def staff_job(request,idd):
    obj = JobId.objects.get(job_id=idd)
    context = {
        'oo': obj
    }
    return render(request,'job/staff_job.html',context)


class Apply_job(APIView):
    def post(self,request):
        obj=Application()
        obj.user_id=request.data['uid']
        obj.job_id=request.data['jid']
        obj.date=datetime.today()
        obj.time=datetime.now()
        obj.status="pending"
        obj.save()
        return HttpResponse('ooo')



def viewapplication(request):
    obj=Application.objects.all()
    context={
        'a':obj
    }
    return render(request,'job/view_application.html',context)

def accept(request,idd):
    obj=Application.objects.get(application_id=idd)
    obj.status="accepted"
    obj.save()
    return viewapplication(request)


def reject(request,idd):
    obj=Application.objects.get(application_id=idd)
    obj.status="rejected"
    obj.save()
    return viewapplication(request)

def more(request,idd):
    obj = Application.objects.get(application_id=idd)
    context={
        'oo':obj
    }
    return render(request,'job/application_details.html',context)

class view_status(APIView):
    def post(self,request):
        obj=Application.objects.filter(user_id=request.data['dddd'])
        ser=android_seriliser1(obj,many=True)
        return Response(ser.data)



class application_history(APIView):
    def post(self,request):
        obj=Application.objects.filter(user_id=request.data['kkk'])
        ser=android_seriliser1(obj,many=True)
        return Response(ser.data)