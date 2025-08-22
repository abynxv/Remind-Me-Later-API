from .serializers import ReminderSerializer, Reminder


class ReminderService:
    @staticmethod
    def create(reminder_data):
        serializer = ReminderSerializer(data=reminder_data)
        serializer.is_valid(raise_exception=True)
        reminder = serializer.save()
        return reminder
    
    @staticmethod
    def list():
        return Reminder.objects.all()