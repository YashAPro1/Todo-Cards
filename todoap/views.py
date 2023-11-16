from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TodomodelSerializers,UsermodelSerializers,UsernewmodelSerializers
from . models import Todomodel,User
from django.contrib import messages 
from rest_framework import status
import bcrypt
from django.shortcuts import render, HttpResponse, redirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from . import models
# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def apiOverView(requests):

    api_urls = {
        'List':'/task-list/',
        'Delete':'/task-delete/<str:pk>/',
    }

    return Response(api_urls)       

@api_view(['GET'])
def taskList(requests,pk):
    tasks = Todomodel.objects.filter(user = pk)
    serializer = TodomodelSerializers(tasks,many=True)
    return Response(serializer.data)



@api_view(['GET'])
def taskDetail(requests, pk):
    tasks = Todomodel.objects.get(id = pk)
    serializer = TodomodelSerializers(tasks,many=False)
    return Response(serializer.data)



@api_view(['Post'])
def taskCreate(requests):
    
    serializer = TodomodelSerializers(data = requests.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['Post'])
def taskUpdate(requests,pk):
    task = Todomodel.objects.get(id = pk)
    serializer = TodomodelSerializers(instance = task,data = requests.data)

    if serializer.is_valid():
        serializer.save(user = requests.user)
    return Response(serializer.data)

    
@api_view(['Post',"PUT"])
def taskUpdate(requests,pk):
    task = Todomodel.objects.get(id = pk)
    serializer = TodomodelSerializers(instance = task,data = requests.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(requests,pk):
    task = Todomodel.objects.get(id = pk)
    task.delete()
    return Response("Items Succesfully deleted!!")

# @api_view(['POST'])
# def handlelogin(request):
#     if request.method == 'POST':




@api_view(["GET","POST"])
@csrf_exempt
def Login(requests):
    
    username = requests.POST['username']
    password = requests.POST['password']
    password = password.encode('utf-8')
    
    try:
        
            
        instructor = models.User.objects.get(UserName = username)
        inspassword = instructor.password.encode('utf-8')
        print(inspassword)
        print(password)
        if bcrypt.checkpw(password, inspassword):
            
            return JsonResponse({'bool':True,'msg':"Welcome",'Userid':instructor.id,"Username":instructor.UserName})
        else:
            return JsonResponse({'bool':False,'msg':"Incorrect Credentials"})
    except:
        return JsonResponse({'bool':False,'msg':"Incorrect Credentials"})


@api_view(["POST"])
@csrf_exempt
def signUp(request):
    if request.method == 'POST':
        tempdict = request.data.copy() # Empty initially
        pwd = tempdict["password"]
        bytePwd = pwd.encode('utf-8')
        mySalt = bcrypt.gensalt()
        pwd_hash = bcrypt.hashpw(bytePwd, mySalt)
        tempdict['password'] = pwd_hash
        print(tempdict)
        serializer = UsermodelSerializers(data=tempdict)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response("", status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
