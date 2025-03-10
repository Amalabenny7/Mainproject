from django.conf.urls import url
from staff import views

urlpatterns = [
    url('add_staff/', views.add_staff),
    url('manage/', views.mng_staff),
    url('edit/(?P<idd>\w+)', views.edit),
    url('block/(?P<idd>\w+)', views.block),
    # url('block/(?P<idd>\w+)', views.block),

]