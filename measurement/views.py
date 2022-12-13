from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from measurement.models import Measurement, Sensor
from measurement.serializers import SensorListCreateSerializer, SensorUpdateSerializer, SensorDetailSerializer, MeasurementCreateSerializer


class SensorListCreateView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorListCreateSerializer

class SensorUpdateDetailView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SensorDetailSerializer
        else:
            return SensorUpdateSerializer

class MeasurementCreateView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementCreateSerializer