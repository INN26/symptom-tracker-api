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
        symptoms = Symptom.objects.filter(user=request.user)
        print('Filtering by symptom while request is:', request.query_params)
        if not symptoms.exists():
            return Response({"message": "No symptoms found for this user."}, status=status.HTTP_404_NOT_FOUND)
        if request.query_params.get('symptom'):
            symptoms = symptoms.filter(symptom_type=request.query_params.get('symptom'))
        trends = symptoms.extra({'day': "date(date_logged)"}).values('day').annotate(count=Count('id')).order_by('day')

        # Format the data a bit
        trend_data = [{"date": item["day"], "count": item["count"]} for item in trends]
        return Response(trend_data, status=status.HTTP_200_OK)
