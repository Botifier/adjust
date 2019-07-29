from rest_framework import serializers

from .models import SampleDataSet


class SampleDataSetSerializer(serializers.ModelSerializer):
    cpi = serializers.FloatField(default=0)
    
    class Meta:
        model = SampleDataSet
        exclude = ('id',)