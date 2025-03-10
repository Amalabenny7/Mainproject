from django.conf.urls import url
from temp import views
urlpatterns = [
    url('admin/',views.admin),
    url('home/',views.home),
    url('staff/',views.staff),
    url('user/',views.user),
    url('base/',views.base),
    url('job/',views.job),
    # url('home23/',views.home23)
]