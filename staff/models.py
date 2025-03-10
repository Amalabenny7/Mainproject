from django.db import models

# Create your models here.
class StaffId(models.Model):
    staff_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    place = models.CharField(max_length=45)
    ph_no = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    dob = models.DateField()
    photo = models.CharField(max_length=550)
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'staff_id'