from django.http import HttpResponse
from .models import Todo

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .serializers import TodoSerializer

def index(request):
    return HttpResponse("Olá mundo! Este é o app todo de Tecnologias Web do Insper.")


@api_view(['GET', 'POST'])
def api_all_tasks(request):
    if request.method == 'POST':
        new_task_data = request.data
        print(new_task_data)
        task = Todo(description=new_task_data["description"], dueDate=new_task_data["dueDate"])
        task.save()
    try:
        all_tasks = Todo.objects.all()
    except Todo.DoesNotExist:
        raise Http404()
    
    serialized_todo= TodoSerializer(all_tasks, many=True)
    return Response(serialized_todo.data)


@api_view(['DELETE'])
def api_delete_task(request, task_id):
    try:
        task = Todo.objects.get(id=int(task_id))
        task.delete()
    except Todo.DoesNotExist:
        raise Http404()