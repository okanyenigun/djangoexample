from rest_framework.views import APIView
from resttest.models import F1Driver
from resttest.serializers import F1DriverSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

class F1DriverCreateView(APIView):
    """create view"""
    def post(self, request):
        f1driver = F1Driver.objects.create()
        serializer = F1DriverSerializer(f1driver)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class F1DriverList(generics.ListAPIView):
    """get view"""
    queryset = F1Driver.objects.all()
    serializer_class = F1DriverSerializer

class F1DriverUpdateView(generics.UpdateAPIView):
    """update view"""
    queryset = F1Driver.objects.all()
    serializer_class = F1DriverSerializer