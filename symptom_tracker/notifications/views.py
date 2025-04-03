from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import NotificationSerializer
from .models import Notification

class NotificationCreateView(generics.CreateAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only return notifications for the logged-in user.
        return Notification.objects.filter(user=self.request.user)
