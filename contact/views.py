from django.shortcuts import render
from contact.models import ContactTb
from staff.models import StaffId

# Create your views here.

def add_contact(request):
    ob = StaffId.objects.all()
    context = {
        'a': ob
    }
    if request.method=="POST":
        obj = ContactTb()
        obj.contact_no=request.POST.get('cn')
        obj.contact_name=request.POST.get('cname')
        obj.remark = 'no remarks'
        obj.staff_id=request.POST.get('staff')
        obj.job_id=1
        obj.mail=request.POST.get('email')
        obj.status='active'
        obj.save()
        return manage_contact(request)
    return render(request, 'contact/add_contact.html',context)

# def manage_contact(request):
#     obj = ContactTb.objects.all().order_by('-contact_id')
#     context = {
#         'a': obj
#     }
#     return render(request, 'contact/manage_contact.html',context)
def manage_contact(request):
    if request.method == "POST":
        search_query = request.POST.get("bk", "").strip()

        contact = ContactTb.objects.all().order_by('-contact_id')
        if search_query:
            # Try to match the search query to job name, location, or date
            contact = contact.filter(contact_name__icontains=search_query)


        return render(request, "contact/manage_contact.html", {"jobs": contact})
    else:
        uuh=ContactTb.objects.all().order_by('-contact_id')
        context={
            "a":uuh
        }

    # obj=JobId.objects.all().order_by('-job_id')
    # context={
    #     'kk':obj
    # }
    return render(request,'contact/manage_contact.html',context)



def block_contact(request,idd):
    obj = ContactTb.objects.get(contact_id=idd)
    obj.status='BLOCKED'
    obj.save()
    return manage_contact(request)



def edit_contact(request,idd):
    ob = ContactTb.objects.get(contact_id=idd)
    context = {
        'a': ob
    }
    if request.method=="POST":
        obj = ContactTb.objects.get(contact_id=idd)
        obj.contact_no=request.POST.get('cn')
        obj.contact_name=request.POST.get('cname')
        obj.mail=request.POST.get('email')
        obj.save()
        return manage_contact(request)
    return render(request, 'contact/edit_contact.html',context)


def view_and_add_remarks(request):
    ss=request.session["u_id"]
    print(ss)
    obj = ContactTb.objects.filter(staff_id=ss).order_by('-contact_id')
    # obj=ContactTb.objects.filter()
    context = {
        'a': obj
    }
    return render(request, 'contact/view_contact_and_add_remarks.html',context)


def remarks(request,idd):
    if request.method=='POST':
        obj=ContactTb.objects.get(contact_id=idd)
        obj.remark=request.POST.get('Remark')
        obj.save()
        return view_and_add_remarks(request)
    return render(request,'contact/remark.html')