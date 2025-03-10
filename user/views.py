from django.http import HttpResponse
from django.shortcuts import render
from user.models import User
from login.models import Login
from rest_framework.views import APIView,Response
from user.serializers import android_seriliser

class user_reg(APIView):
    def post(self,request):
        obj=User()
        obj.name = request.data['name']
        obj.place = request.data['place']
        obj.ph_no = request.data['ph_no']
        obj.email = request.data['email']
        obj.photo = request.data['photo']
        obj.dob = request.data['dob']
        obj.interest = request.data['interest']
        obj.gender = request.data['gender']
        obj.hobbies = request.data['hobbies']
        obj.cv = request.data['cv']
        obj.cert_id = 1
        obj.adrees = request.data['adrees']
        obj.qualification = request.data['qualification']
        obj.pincode = request.data['pincode']
        obj.password = request.data['password']
        obj.username=request.data['username']
        obj.save()

        ob=Login()
        ob.username=obj.username
        ob.password=obj.password
        ob.u_id=obj.reg_id
        ob.type='user'
        ob.save()
        return HttpResponse('yes')

from keen_job import settings
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def upimage(request):
    if request.method=="POST" and request.FILES['file']:
        mfile=request.FILES['file']
        fs=FileSystemStorage()
        fpath=str(settings.BASE_DIR) + (settings.STATIC_URL) + mfile.name
        fname=fs.save(fpath, mfile)
        usobj=User.objects.all().order_by('-reg_id')
        uob=usobj[0]
        uob.photo=fname
        uob.save()
        print(fname)
        return HttpResponse("yess")

@csrf_exempt
def photo(request):
    if request.method=="POST" and request.FILES['file']:
        mfile=request.FILES['file']
        fs=FileSystemStorage()
        fpath=str(settings.BASE_DIR) + (settings.STATIC_URL) + mfile.name
        fname=fs.save(fpath, mfile)
        usobj = User.objects.all().order_by('-reg_id')
        uob = usobj[0]
        uob.cv = fname
        uob.save()
        print(fname)
        return HttpResponse("yess")


def view_user(request):
    obj=User.objects.all()
    context={
        'vw':obj
    }
    return render(request,'user/view_user.html',context)

def mng_user(request):
    obj=User.objects.all()
    context={
        'a':obj
    }

    return render(request, 'user/manage.html',context)

def block(request,idd):
    obj=User.objects.get(reg_id=idd)
    obj.status='blocked'
    obj.save()
    return mng_user(request)

