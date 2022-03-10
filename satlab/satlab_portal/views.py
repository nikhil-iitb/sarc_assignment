from django.shortcuts import render
from django.http import HttpResponse
from .forms import Student
from .models import Student
from . import serializers 
from rest_framework import viewsets  
from rest_framework.decorators import api_view    
from rest_framework.response import Response
from . import models
from django.core.mail import send_mail

# Create your views here.

def index(request):
    return HttpResponse("Welcome to Satlab")

# def register(request):
#     if request.method == "POST":
#         form = Student(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Thanks')
    
#     else:
#         form = Student()

#     return render(request, 'name.html', {'form': form})

@api_view(['POST'])
def register(request):
    req_data = request.data
    # email = request.data['email']
    # otp = 123456
    # res1 = send_mail("hello nikhil", otp, "nikhiltiwari1912@gmail.com", [email])
    print("Entered the register view ")
    person, created = models.Student.objects.get_or_create(name = req_data['name'])
    if created:
        person.name = req_data['name']
        person.email = req_data['email']
        print(person.email)
        person.save()
        person_serializer = serializers.StudentSerializer(person)
        return Response(person_serializer.data)
    else:
        if req_data['password'] == 12345:
            person.verified = 1
            person.save()
            return Response({'status': 'Verified'}) 

@api_view(['POST'])
def postfeed(request):
    req_data = request.data
    name1 = request.query_params.get('id')
    print("My name", name1)
    print("My post", req_data)
    student = Student.objects.filter(name = name1).update(postfeed = req_data)
    # student.postfeed = req_data
    
    return Response({'status': 'Post successfully saved'})
        
@api_view(['GET'])
def feed(request):
    print("Printing the feeds")
    student = Student.objects.all()
    feedserialiser = serializers.StudentSerializer(student)
    return Response(student)