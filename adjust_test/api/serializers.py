from rest_framework import serializers

from .models import SampleDataSet


class SampleDataSetSerializer(serializers.ModelSerializer):
    cpi = serializers.FloatField(default=0)

    # Source: https://www.django-rest-framework.org/api-guide/serializers/#example
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        fields = self.context['request'].query_params.get('fields')
        if fields:
            fields = fields.split(',')
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = SampleDataSet
        exclude = ('id',)