from rest_framework import serializers

from .models import SampleDataSet


class SampleDataSetSerializer(serializers.ModelSerializer):

        class Meta:
            model = SampleDataSet
            exclude = ('id',)