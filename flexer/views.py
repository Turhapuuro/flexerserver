from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import datetime
from flexer.models import User, Client, Project, Task
from flexer.serializers import UserSerializer, ClientSerializer, ProjectSerializer, TaskSerializer


# USERS
@csrf_exempt
def user_list(request):
    # List all users
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)


# CLIENTS
@csrf_exempt
def fetch_clients(request):
    # Fetch all clients
    if request.method == 'GET':
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return JsonResponse(serializer.data, safe=False)

    # Create new client
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        serializer = ClientSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def manage_client(request, pk):
    # Check if project exists
    try:
        client = Client.objects.get(pk=pk)
    except Client.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'DELETE':
        client.delete()
        return JsonResponse(pk, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ClientSerializer(client, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


# PROJECTS
@csrf_exempt
def fetch_projects(request):
    # Fetch all projects
    if request.method == 'GET':
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return JsonResponse(serializer.data, safe=False)

    # Create new project
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def manage_project(request, pk):
    # Check if project exists
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'DELETE':
        project.delete()
        return JsonResponse(pk, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProjectSerializer(project, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

# TASKS
@csrf_exempt
def fetch_tasks(request):
    # Fetch all tasks
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(serializer.data, safe=False)

    # Create new task
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def manage_task(request, pk):
    # Check if task exists
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'DELETE':
        task.delete()
        return JsonResponse(pk, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(task, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def tasks_overview(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        first_day = data['first_day']
        last_day = data['last_day']
        tasks = Task.objects.filter(date__range=(first_day, last_day))
        serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(serializer.data, safe=False)
