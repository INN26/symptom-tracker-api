from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Symptom
from .serializers import SymptomSerializer
from django.db.models import Count
from django.utils.dateformat import DateFormat
from django.utils import timezone

class SymptomViewSet(viewsets.ModelViewSet):
    serializer_class = SymptomSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only allow users to view their own symptoms
        return Symptom.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SymptomTrendsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print("Attempted Get request to SymptomTrendsView")
        # Basic example: count symptoms per day for the current user.
        symptoms = Symptom.objects.filter(user=request.user)
        trends = symptoms.extra({'day': "date(date_logged)"}).values('day').annotate(count=Count('id')).order_by('day')
        # Format the data a bit
        trend_data = [{"date": item["day"], "count": item["count"]} for item in trends]
        return Response(trend_data, status=status.HTTP_200_OK)
