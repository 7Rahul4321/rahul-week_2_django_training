from django.shortcuts import render

def home(request):

    students = [
        {"name": "Rahul", "branch": "CSE", "year": "2nd"},
        {"name": "Aman", "branch": "AI/ML", "year": "3rd"},
        {"name": "Priya", "branch": "IT", "year": "2nd"},
        {"name": "Rohit", "branch": "Data Science", "year": "1st"}
    ]

    return render(request, 'students/home.html', {'students': students})