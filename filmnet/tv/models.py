from django.db import models

# Create your models here.
class TvStation(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField()
    
    def __str__(self):
        return self.name
    
    
class TvProgram(models.Model):
    name = models.CharField(max_length=50)
    tv_station = models.ForeignKey(TvStation, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    adults_only = models.BooleanField()
    
    def __str__(self):
        return self.name