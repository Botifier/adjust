from django.conf.urls import url
from .views import SampleDataSetView


urlpatterns = [
    url('sampledataset/', SampleDataSetView.as_view(), name="sample-data-set-list"),
]