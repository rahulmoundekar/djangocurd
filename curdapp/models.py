from django.db import models


# Create your models here.

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    email = models.EmailField()
    contact = models.CharField(max_length=15)

    class Meta:
        db_table = 'employee'
