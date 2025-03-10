from django.conf.urls import url
from job import views

urlpatterns = [
    url('add_job/',views.add_job),
    url('manage/', views.manage),
    url('edit/(?P<idd>\w+)',views.edit),
    url('delete/(?P<idd>\w+)',views.delete),
    url('view/',views.view),
    url('view_job_new/',views.view_job_new),
    url('vwww/', views.vwwww.as_view()),
    url('job_details/(?P<idd>\w+)',views.view_job_details),
    url('job_apply/', views.Apply_job.as_view()),
    url('application/',views.viewapplication),
    url('accept/(?P<idd>\w+)',views.accept),
    url('reject/(?P<idd>\w+)',views.reject),
    url('mores/(?P<idd>\w+)',views.more),
    url('view_stat/', views.view_status.as_view()),
    url('history/', views.application_history.as_view()),
    url('staff_job/(?P<idd>\w+)/', views.staff_job)

]