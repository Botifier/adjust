from django.db.models import FloatField, Sum, Avg
from django.db.models.functions import Cast

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
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filter_class = SampleDataSetFilter
    ordering_fields = '__all__'

    def get_queryset(self):
        queryset = SampleDataSet.objects.all()
        group_fields = self.request.query_params.get('group')
        aggregation_fields = self.request.query_params.get('aggregation')
        if group_fields:
            queryset = queryset.values(*group_fields.split(','))
            if aggregation_fields:
                for field in aggregation_fields.split(','):
                    if field == 'impressions':
                        queryset = queryset.annotate(impressions=Sum('impressions'))
                    elif field == 'clicks':
                        queryset = queryset.annotate(clicks=Sum('clicks'))
                    elif field == 'installs':
                        queryset = queryset.annotate(installs=Sum('installs'))
                    elif field == 'spend':
                        queryset = queryset.annotate(spend=Sum('spend'))
                    elif field == 'revenue':
                        queryset = queryset.annotate(revenue=Sum('revenue'))
                    elif field == 'cpi':
                        queryset = queryset.annotate(cpi=Sum('spend')/Cast(Sum('installs'), FloatField()))
        return queryset
