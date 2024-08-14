from rest_framework import generics
from .models import Tasks
from .serializers import TasksSerializer


class TasksList(generics.ListCreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer


class TasksDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer

