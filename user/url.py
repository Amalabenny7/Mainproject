from django.conf.urls import url
from user import views

urlpatterns = [
    url('user/',views.user_reg.as_view()),
    url('cvup/',views.upimage),
    url('photo/',views.photo),
    url('vvv/',views.view_user),
    url('manage/', views.mng_user),
    url('block/(?P<idd>\w+)', views.block),
]