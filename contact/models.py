from django.db import models
from staff.models import StaffId

# Create your models here.
class ContactTb(models.Model):
    contact_id = models.AutoField(primary_key=True)
    contact_no = models.CharField(max_length=45)
    contact_name = models.CharField(max_length=45)
    remark = models.CharField(max_length=45)
    job_id = models.IntegerField()
    mail = models.CharField(max_length=45)
    status = models.CharField(max_length=45)
    # staff_id = models.IntegerField()
    staff=models.ForeignKey(StaffId,models.CASCADE)
    class Meta:
        managed = False
        db_table = 'contact_tb'
