from django.http import HttpResponse
from .models import Todo

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .serializers import TodoSerializer

def index(request):
    return HttpResponse("Olá mundo! Este é o app todo de Tecnologias Web do Insper.")


@api_view(['GET', 'POST', 'DELETE'])
def api_todo(request):
    if request.method == 'POST':
        print("POST")
        # new_user_data = request.data
        # try:
        #     user = User.objects.get(username=username)
        #     user.cities = new_user_data['cities']
        #     print("try")
        # except:
        #     user = User(username=username)
        #     print("except")
        # user.save()
    else:
        try:
            all_tasks = Todo.objects.all()
        except Todo.DoesNotExist:
            raise Http404()
    
    serialized_note = TodoSerializer(all_tasks, many=True)
    return Response(serialized_note.data)