from django.urls import path

from measurement.views import SensorListCreateView, SensorUpdateDetailView, MeasurementCreateView


urlpatterns = [
    path('sensors/', SensorListCreateView.as_view()),
    path('sensors/<pk>/', SensorUpdateDetailView.as_view()),
    path('measurements/', MeasurementCreateView.as_view()),
]
