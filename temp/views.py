from django.shortcuts import render
from job.models import JobId
# Create your views here.
def admin(request):
    return render(request,'temp/admin.html')
# def home(request):
#     vv=request.POST.get('bk')
#     if request.method=="POST":
#         obj = JobId.objects.filter(jobtitle__icontains=vv)
#         context = {
#             'oo': obj
#         }
#         return render(request, 'temp/home.html', context)
#     else:
#         obj=JobId.objects.all()
#         context={
#             'oo':obj
#         }
#     return render(request,'temp/home.html',context)
def staff(request):
    return render(request, 'temp/staff.html')
def user(request):
    return render(request, 'temp/user.html')

def base(request):
    return render(request, 'temp/adminbase.html')

def job(request):
    obj = JobId.objects.all()
    context = {
        'oo': obj
    }
    return render(request,'temp/job.html',context)


from django.shortcuts import render
from job.models import JobId
from datetime import datetime


def home(request):
    if request.method == "POST":
        search_query = request.POST.get("bk", "").strip()

        jobs = JobId.objects.all()
        if search_query:
            # Try to match the search query to job name, location, or date
            jobs = jobs.filter(jobtitle__icontains=search_query) | jobs.filter(location__icontains=search_query)

            # Check if the input is a valid date
            try:
                search_date = datetime.strptime(search_query, "%Y-%m-%d").date()
                jobs = jobs | JobId.objects.filter(last_date=search_date)  # Ensure your Job model has 'posted_date'
            except ValueError:
                pass  # If it's not a date, ignore this part

        return render(request, "temp/home.html", {"jobs": jobs})
    else:
        uuh=JobId.objects.all()
        context={
            "jobs":uuh
        }

    return render(request, "temp/home.html",context)
