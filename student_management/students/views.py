from django.shortcuts import render, redirect
from .models import Student

def home(request):

    if request.method == "POST":
        name = request.POST['name']
        branch = request.POST['branch']
        year = request.POST['year']

        Student.objects.create(
            name=name,
            branch=branch,
            year=year
        )

        return redirect('/')

    students = Student.objects.all()

    return render(request, 'students/home.html', {'students': students})
def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()

    return redirect('/')
def update_student(request, id):

    student = Student.objects.get(id=id)

    if request.method == "POST":
        student.name = request.POST['name']
        student.branch = request.POST['branch']
        student.year = request.POST['year']

        student.save()

        return redirect('/')

    return render(request, 'students/update.html', {'student': student})