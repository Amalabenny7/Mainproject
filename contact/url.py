from django.conf.urls import url
from contact import views

urlpatterns=[
    url('add_contact/', views.add_contact),
    url('manage/', views.manage_contact),
    url('block/(?P<idd>\w+)', views.block_contact),
    url('edit/(?P<idd>\w+)', views.edit_contact),
    url('view_and_add_remark/',views.view_and_add_remarks),
    url('remark/(?P<idd>\w+)', views.remarks)
]