from django.shortcuts import render
from login.models import Login
from django.http import HttpResponseRedirect

# Create your views here.
#
# Create your views here.
def login(request):
    if request.method =="POST":
        uname =request.POST.get("un")
        passw =request.POST.get("ps")
        obj =Login.objects.filter(username=uname,password=passw)
        tp=""
        for ca in obj:
             tp = ca.type
             uid = ca.u_id
             if tp =="admin":
                request.session["u_id"] = uid
                return HttpResponseRedirect('/temp/admin/')
             elif tp =="user":
                request.session["u_id"] = uid
                return HttpResponseRedirect('/temp/user/')
             elif tp =="staff":
                request.session["u_id"] = uid
                return HttpResponseRedirect('/temp/staff/')
             else:
                objlist = "username or password incorret....please try again....!"
                context = {
                    'msg':objlist
                }
                return render(request,'login/login.html',context)
    return render(request,'login/login.html')

from rest_framework.views import APIView,Response
from login.serializers import android_seriliser


class login_flutter(APIView):
    def get(self,request):
        ob = Login.objects.all()
        ser = android_seriliser(ob,many=True)
        return Response(ser.data)

    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        ob = Login.objects.filter(username=username, password=password)
        ser = android_seriliser(ob, many=True)
        return Response(ser.data)


