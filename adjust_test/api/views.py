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
        fields = self.request.query_params.get('fields')
        group_fields = self.request.query_params.get('group')
        if group_fields:
            queryset = queryset.values(*group_fields.split(','))
            if fields:
                fields = fields.split(',')
                if 'cpi' in fields:
                    queryset = queryset.annotate(cpi=Sum('spend')/Cast(Sum('installs'), FloatField()))
                if 'impressions' in fields:
                    queryset = queryset.annotate(impressions=Sum('impressions'))
                if 'clicks' in fields:
                    queryset = queryset.annotate(clicks=Sum('clicks'))
                if 'installs' in fields:
                    queryset = queryset.annotate(installs=Sum('installs'))
                if 'spend' in fields:
                    queryset = queryset.annotate(spend=Sum('spend'))
                if 'revenue' in fields:
                    queryset = queryset.annotate(revenue=Sum('revenue'))
        return queryset
