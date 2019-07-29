from rest_framework import generics, filters

from django_filters.rest_framework import DjangoFilterBackend, FilterSet, DateFilter

from .models import SampleDataSet
from .serializers import SampleDataSetSerializer


class SampleDataSetFilter(FilterSet):
    date_from = DateFilter(field_name='date', lookup_expr='gte')
    date_to = DateFilter(field_name='date', lookup_expr='lte')

    class Meta:
        model = SampleDataSet
        fields = ['date', 'channel', 'country', 'os']


class SampleDataSetView(generics.ListAPIView):
    serializer_class = SampleDataSetSerializer
    queryset = SampleDataSet.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filter_class = SampleDataSetFilter
    ordering_fields = '__all__'
