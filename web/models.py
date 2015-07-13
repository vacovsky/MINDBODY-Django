


from django.db import models
from django.contrib.auth.models import User

class ReportsCacheModel(models.Model):
  id = models.AutoField(primary_key=True)
  datapull_datestamp = models.DateField(auto_now_add=True)
  chart_name = models.CharField(max_length=50)
  data_string = models.TextField()

  def __str__(self):
    return "Cached Chart Data by Day"