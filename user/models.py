from django.db import models

class User(models.Model):
    reg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    place = models.CharField(max_length=45)
    ph_no = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    photo = models.CharField(max_length=45)
    dob = models.DateField(db_column='DOB')  # Field name made lowercase.
    interest = models.CharField(max_length=45)
    gender = models.CharField(max_length=45)
    hobbies = models.CharField(max_length=45)
    cv = models.CharField(max_length=45)
    cert_id = models.IntegerField()
    adrees = models.CharField(max_length=45)
    pincode = models.CharField(max_length=45)
    qualification = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    status = models.CharField(max_length=45, blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'user'


