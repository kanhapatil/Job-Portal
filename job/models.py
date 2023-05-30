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
    

# CREATE MODEL FOR ADD JOB
class Job(models.Model):
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    title = models.CharField(max_length=100)
    salary = models.FloatField(max_length=20)
    image = models.FileField()
    description = models.CharField(max_length=500)
    experience = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    skills = models.CharField(max_length=100)
    creationdate = models.DateField()

    def __str__(self):
        return self.title 