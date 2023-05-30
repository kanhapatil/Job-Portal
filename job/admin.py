from django.contrib import admin
from .models import StudentUser, Recruiter, Job

# REGISTER STUDENTUSER MODEL
admin.site.register(StudentUser)

# REGISTER RECRUITER MODEL
admin.site.register(Recruiter)

# REGISTER JOB MODEL
admin.site.register(Job)
