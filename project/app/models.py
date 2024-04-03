from django.db import models


# Create your models here.
class student(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    City=models.CharField(max_length=50)
    Contact = models.CharField(max_length=50)
    Add = models.CharField(max_length=50,null=True)


    class Meta:
        ordering = ["Name"]
        # ordering = ["-Name"]
        verbose_name = "stu"
        # verbose_name_plural = 'student'
