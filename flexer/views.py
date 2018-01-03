from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from flexer.models import User, Task, Snippet
from flexer.serializers import UserSerializer, TaskSerializer, SnippetSerializer

# Create your views here.
#def index(request):
 #   return render(request, 'flexer/index.html')

@csrf_exempt
def user_list(request):
    """
    List all users
    """
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def manage_tasks(request):
    """
    Fetch all tasks
    """
    tasks = Task.objects.all()

    if request.method == 'GET':
        serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def delete_tasks(request):
    """
    Fetch all tasks
    """
    print(request)
    print(request.data)
   # if request.method == 'DELETE':
    #    task = Task.objects.get(task_id=request.DELETE['id'])
     #   task.delete()
      #  return HttpResponse(status=204)

@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)