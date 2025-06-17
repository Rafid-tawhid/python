from django.http import JsonResponse
from django.shortcuts import render
from students.models import Student
def studentView(request):
    students=Student.objects.all()
    print(students)
    students_list=list(students.values())
    return JsonResponse(students_list,safe=False)