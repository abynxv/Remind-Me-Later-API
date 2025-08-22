from django.urls import path
from .views import ReminderViewSet

urlpatterns = [
    path('reminder/', ReminderViewSet.as_view({'get': 'list', 'post': 'create'})),
]