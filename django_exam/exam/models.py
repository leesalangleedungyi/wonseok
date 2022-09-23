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
            # 테이블명 ( defalut : 앱이름_클래스명)
        db_table = 'album'
        
    def __str__(self) -> str:
        return self.name
    
class Person2(models.Model):
    SHIRT_SIZE= (
        ("S","Small"),
        ("M","Medium"),
        ("L","Large"),
        
        )
    
    name = models.CharField(max_length=60)
    shirt_size= models.CharField(max_length=1,choices=SHIRT_SIZE)
    
    class Meta:
        # 테이블명 ( defalut : 앱이름_클래스명)
        db_table = 'person2'
    def __str__(self) -> str:
        return self.name + "." + self.shirt_size
    
class Runner(models.Model):
    Medal_Type = models.TextChoices("MedalType","Gold Silver Bronze")
    name=models.CharField(max_length=60,blank=False)
    medal=models.CharField(blank=True,choices=Medal_Type.choices,max_length=10)
    #blank = 내용이 안들어오는지 오는지 확인 True면 안들어와도댐
    
    class Meta:
        db_table = "runner"
    def __str__(self) -> str:
        return self.name + "." + self.medal
    
    
    
class Fruit(models.Model):
    #name 필드 : primary_key= Ture
    # primary_key = not null , unique 개념 (무조건 들어와야하고 중복되면 안됌)
    name = models.CharField(max_length=100,primary_key=True)
    
    def __str__(self) -> str:
        return self.name
    
class Question(models.Model):
    question_text=models.CharField(max_length=200,verbose_name='질문')
    pub_date=models.DateTimeField(verbose_name='작성날짜')
    
    def __str__(self) -> str:
        return self.question_text
    
class Choice(models.Model):
    #question = models.ForeignKey(Question,on_delete=models.CASCADE,verbose_name='the related Question')
    choice_text=models.CharField(max_length=200)
    votes = models.IntegerField(default=0,verbose_name='투표')
    
    def __str__(self) -> str:
        return self.choice_text
    