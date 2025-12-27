from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import Marks,Student
from .forms import StudentForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def home_page(request):
    marks=Marks.objects.all()
    total=0
    for i in marks:
        total=i.math_mark+i.english_mark+i.malayalam_mark
        i.total=total
        i.avg=total/3
    if request.GET.get('class'):
        class_name=request.GET.get('class')
        marks=marks.filter(student__class_name__name=class_name)
    elif request.GET.get('division'):
        division=request.GET.get('division')
        marks=marks.filter(student__division__name=division)

    return render(request,'home.html',{'marks':marks,'total':total})

def admin_login(request):
    if request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user.is_staff:
            login(request,user)
            return redirect('admin_dash')
    return render(request,'admin_login.html')

@login_required(login_url='admin_login')
def admin_logout(request):
    logout(request)
    return redirect('home')

@login_required(login_url='admin_login')
def admin_dashboard(request):
    student=Student.objects.all()
    return render(request,'admin.html',{'std':student})

@login_required(login_url='admin_login')
def create_student(request):
    if request.POST:
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dash')
    else:
        form=StudentForm()
    return render(request,'add_student.html',{'form':form})

@login_required(login_url='admin_login')
def edit_student(request,id):
    std=Student.objects.get(id=id)
    if request.POST:
        form=StudentForm(request.POST,instance=std)
        if form.is_valid():
            form.save()
            return redirect('admin_dash')
    else:
        form=StudentForm(instance=std)
    return render(request,'add_student.html',{'form':form})

@login_required(login_url='admin_login')
def delete_student(request,id):
    std=Student.objects.get(id=id)
    std.delete()
    return redirect('admin_dash')