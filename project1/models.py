from django.db import models

class case(models.Model):
    case_id=models.CharField(primary_key=True,max_length=15)
    victim_name=models.CharField(max_length=255)
    io_name=models.CharField(max_length=70)
    io_id=models.CharField(max_length=15)
    crime_date=models.DateTimeField(blank=True)
    category=models.CharField(max_length=70)
    victim_id=models.CharField(max_length=15)
    crime_loc=models.CharField(max_length=255)
    
    
