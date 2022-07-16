from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee


# Create your views here.
def employee_view(request):
    # emp = {
    #     'id': 123,
    #     'name': 'John',
    #     'salary': 1000000
    # }

    data = Employee.objects.all()
    response = {'employees': list(data.values('name', 'salary'))}

    return JsonResponse(response)
