from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SymptomViewSet, SymptomTrendsView

router = DefaultRouter()
router.register(r'', SymptomViewSet, 'symptoms')

urlpatterns = [
    path('trends/', SymptomTrendsView.as_view(), name='symptom-trends'),
    path('', include(router.urls)),
]
