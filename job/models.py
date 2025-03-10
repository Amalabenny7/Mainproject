from django.db import models
from user.models import User
from staff.models import StaffId
# Create your models here.


class JobId(models.Model):
    job_id = models.AutoField(primary_key=True)
    jobtitle = models.CharField(max_length=45)
    description = models.CharField(max_length=1000)
    number_of_vacancy = models.CharField(db_column='number of vacancy', max_length=45)  # Field renamed to remove unsuitable characters.
    gender = models.CharField(max_length=45)
    age = models.CharField(max_length=45)
    experience = models.CharField(max_length=45)
    salary = models.CharField(max_length=45)
    working_time = models.CharField(max_length=45)
    c_name = models.CharField(max_length=45)
    c_details = models.CharField(max_length=500)
    location = models.CharField(max_length=45)
    last_date = models.CharField(db_column='last date', max_length=45)  # Field renamed to remove unsuitable characters.
    qualification = models.CharField(max_length=45)
    type = models.CharField(max_length=45)
    statusl = models.CharField(max_length=45)
    other = models.CharField(max_length=45, blank=True, null=True)
    # staff_id = models.IntegerField()
    staff=models.ForeignKey(StaffId,on_delete=models.CASCADE)


    class Meta:
        managed = False
        db_table = 'job_id'




class Application(models.Model):
    application_id = models.AutoField(primary_key=True)
    # reg_id = models.CharField(max_length=45)
    reg = models.ForeignKey(User,on_delete=models.CASCADE)
    # job_id = models.CharField(max_length=45)
    job=models.ForeignKey(JobId,on_delete=models.CASCADE)
    status = models.CharField(max_length=45)
    date = models.CharField(max_length=45)
    time = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'application'
