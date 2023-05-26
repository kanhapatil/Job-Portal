from django.shortcuts import render, redirect
from .models import StudentUser, Recruiter
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# INDEX PAGE
def index(request):
    return render(request, 'index.html')


# ADMIN LOGIN PAGE
def admin_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']

        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error':error}
    return render(request, 'admin_login.html', d)


# ADMIN HOME PAGE
def admin_home(request):
    return render(request, 'admin_home.html')

# USER LOGIN PAGE
def user_login(request):
    error = ''
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']

        user = authenticate(username=u, password=p)
        if user:
            try:
                user1 = StudentUser.objects.get(user=user)
                if user1.type == "student":
                    login(request, user)
                    error = "no"
                else:
                    error = "yes"
            except:
                error = "yes"
        else:
            error = "yes"
    d = {'error':error}
    return render(request, 'user_login.html', d)


# USER SINGUP PAGE
def user_signup(request):
    error = ''
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        i = request.FILES['image']
        p = request.POST['pwd']
        e = request.POST['email']
        con = request.POST['contact']
        gen = request.POST['gender']

        try:
            user = User.objects.create_user(first_name=f, last_name=l, username=e, password=p)
            StudentUser.objects.create(user=user, mobile=con, image=i, gender=gen, type='student')
            error="no"
        except:
            error="yes"
    d = {'error':error}

    return render(request, 'user_signup.html', d)


# USER HOME PAGE
def user_home(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    return render(request, 'user_home.html')

# LOGOUT PAGE
def Logout(request):
    logout(request)
    return redirect('/')
    

# RECRUITER LOGIN PAGE
def recruiter_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']

        user = authenticate(username=u, password=p)
        if user:
            try:
                user1 = Recruiter.objects.get(user=user)
                if user1.type == "recruiter" and user1.status != 'pending':
                    login(request, user)
                    error = "no"
                else:
                    error = "not"
            except:
                error = "yes"
        else:
            error = "yes"
    d = {'error':error}
    return render(request, 'recruiter_login.html', d)


# RECRUITER SINGUP PAGE
def recruiter_signup(request):
    error = ''
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        i = request.FILES['image']
        p = request.POST['pwd']
        e = request.POST['email']
        con = request.POST['contact']
        gen = request.POST['gender']
        company = request.POST['company']

        try:
            user = User.objects.create_user(first_name=f, last_name=l, username=e, password=p)
            Recruiter.objects.create(user=user, mobile=con, image=i, gender=gen, type='recruiter', company=company, status='pending')
            error="no"
        except:
            error="yes"
    d = {'error':error}
    return render(request, 'recruiter_signup.html',d)


# RECRUITER HOME PAGE
def recruiter_home(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login') 
    return render(request, 'recruiter_home.html')


# VIEW USERS PAGE
def view_users(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = StudentUser.objects.all()
    d = {'data':data}
    return render(request, 'view_users.html', d)

# DELETE USER 
def delete_user(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    student = StudentUser.objects.get(id=pid)
    student.delete()
    return redirect('view_users')


# RECRUITER PENDING
def recruiter_pending(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.filter(status="pending")
    d = {'data':data}
    return render(request, 'recruiter_pending.html', d)

# RECRUITER ACCEPTED
def recruiter_accepted(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.filter(status="Accept")
    d = {'data':data}
    return render(request, 'recruiter_accepted.html', d)

# RECRUITER REJECTED
def recruiter_rejected(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.filter(status='Reject')
    d = {'data':data}
    return render(request, 'recruiter_rejected.html', d)

# ALL RECRUITERS
def recruiter_all(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.all()
    d = {'data':data}
    return render(request, 'recruiter_all.html', d)


# CHANGE STATUS
def change_status(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    recruiter = Recruiter.objects.get(id=pid)
    if request.method == 'POST':
        s = request.POST['status']
        recruiter.status = s
        try:
            recruiter.save()
            error = "no"
        except:
            error = "yes"
    d = {'recruiter':recruiter, 'error':error}
    return render(request, 'change_status.html',d)