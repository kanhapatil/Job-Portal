from django.contrib import admin
from .models import StudentUser, Recruiter

# REGISTER STUDENTUSER MODEL
admin.site.register(StudentUser)

# REGISTER RECRUITER MODEL
admin.site.register(Recruiter)
