from platform import release
from django.db import models

# Create your models here.

class person(models.Model):
    # 30글자 안의 성,이름
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
    class Meta:
        
        db_table = "person"
        
    def __str__(self) -> str:
        return self.first_name+","+self.last_name

class Musician(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    instrument = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'msician'
        
    def __str__(self) -> str:
        return self.first_name+","+self.last_name+","+self.instrument


class Album(models.Model):
    #외래키
    
    artist = models.ForeignKey(Musician,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
    
    class Meta:
        db_table = 'album'
        
    def __str__(self) -> str:
        return self.name