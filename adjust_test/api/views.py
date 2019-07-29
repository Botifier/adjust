from rest_framework import generics

from .models import SampleDataSet
from .serializers import SampleDataSetSerializer


class SampleDataSetView(generics.ListAPIView):
    serializer_class = SampleDataSetSerializer
    queryset = SampleDataSet.objects.all()
