from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Student
from .forms import StudentForm

def landing_page(request):
    return render(request, 'landing.html')

def user_login(request):
    if request.user.is_authenticated:
        return redirect('index')  
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            error_message = "Invalid username or password"
            return render(request, 'students/login.html', {'error_message': error_message})
    return render(request, 'students/login.html')

@login_required
def index(request):
    return render(request, 'students/index.html', {
        'students': Student.objects.all()
    })

def user_logout(request):
    logout(request)
    return redirect('login')

def view_student(request, id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student = Student(
                student_number=form.cleaned_data['student_number'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                field_of_study=form.cleaned_data['field_of_study'],
                gpa=form.cleaned_data['gpa']
            )
            new_student.save()
            return render(request, 'students/add.html', {
                'form': StudentForm(),
                'success': True
            })
    else:
        form = StudentForm()
    
    return render(request, 'students/add.html', {
        'form': form
    })

def edit(request, id):
    student = Student.objects.get(pk=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'students/edit.html', {
                'form': form,
                'success': True,
                'student': student
            })
    else:
        form = StudentForm(instance=student)
    
    return render(request, 'students/edit.html', {
        'form': form,
        'student': student
    })

def delete(request, id):
    student = Student.objects.get(pk=id)
    student.delete()
    return HttpResponseRedirect(reverse('index'))