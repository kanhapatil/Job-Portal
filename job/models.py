from django.db import models
from django.contrib.auth.models import User

# CREATE MODEL FOR STUDENT USERS
class StudentUser(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE) 
    mobile = models.CharField(max_length=15, null=True)
    image = models.FileField(null=True)
    gender = models.CharField(max_length=15, null=True)
    type = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.user.username 
    

# CREATE MODEL FOR RECRUUITER USERS
class Recruiter(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE) 
    mobile = models.CharField(max_length=15, null=True)
    image = models.FileField(null=True)
    gender = models.CharField(max_length=15, null=True)
    company = models.CharField(max_length=200, null=True)
    type = models.CharField(max_length=15, null=True)
    status = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.user.username 