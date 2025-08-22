from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from .serializers import ReminderSerializer
from .services import ReminderService


class ReminderViewSet(ViewSet):
    def create(self, request):
        reminder = ReminderService.create(request.data)
        serializer = ReminderSerializer(reminder)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        reminders = ReminderService.list()
        serializer = ReminderSerializer(reminders, many=True)
        return Response(serializer.data)

