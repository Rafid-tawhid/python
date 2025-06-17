from django.http import JsonResponse
from django.shortcuts import render
def studentView(request):
    students={
        'id':1,
        'name':'ratan',
        'class':'CSE'
    }

    return JsonResponse(students)