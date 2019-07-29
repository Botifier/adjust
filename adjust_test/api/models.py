from django.db import models


class SampleDataSet(models.Model):
    date = models.DateField()
    channel = models.CharField(max_length=32)
    country = models.CharField(max_length=2)
    os = models.CharField(max_length=32)
    impressions = models.IntegerField()
    clicks = models.IntegerField()
    installs = models.IntegerField()
    spend = models.FloatField()
    revenue = models.FloatField()

    @property
    def cpi(self):
        return self.spend / self.installs
