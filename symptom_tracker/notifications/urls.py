from django.urls import path
from .views import NotificationCreateView, NotificationListView

urlpatterns = [
    path('list/', NotificationListView.as_view(), name='list-notifications'),
    path('', NotificationCreateView.as_view(), name='create-notification'),
]