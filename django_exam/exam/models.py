from turtle import mode
from django.db import models

# Person
# first_name(30), last_name(30)
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        # 테이블 명 지정(default : 앱이름_클래스명)
        db_table = "person"


    def __str__(self) -> str:
        return self.first_name+", "+self.last_name


# first_name(30), last_name(30), instrument(100)
class Musician(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    instrument = models.CharField(max_length=100)

    class Meta:
        # 테이블 명 지정(default : 앱이름_클래스명)
        db_table = "musician"


    def __str__(self) -> str:
        # return "%s %s %s" % (self.first_name,self.last_name,self.instrument)
        return self.first_name+", "+self.last_name+", "+self.instrument

class Album(models.Model):
    # 외래 키
    # on_delete=models.CASCADE : 부모키가 삭제되면 자식 키도 같이 삭제 
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

    class Meta:
        # 테이블 명 지정(default : 앱이름_클래스명)
        db_table = "album"

    def __str__(self) -> str:        
        return self.name


class Person2(models.Model):
    SHIRT_SIZE = (
        ("S","Small"),
        ("M","Medium"),
        ("L","Large"),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1,choices=SHIRT_SIZE)

    class Meta:       
        db_table = "person2"

    def __str__(self) -> str:
        return self.name + ". " +self.shirt_size

class Runner(models.Model):
    Medal_Type = models.TextChoices("MedalType","GOLD SILVER BRONZE")
    name = models.CharField(max_length=60)
    medal = models.CharField(blank=True, choices=Medal_Type.choices,max_length=10)

    def __str__(self) -> str:
        return self.name + ". " +self.medal

class Fruit(models.Model):
    # name 필드 : primary_key=True
    # primary key : not null, unique
    name = models.CharField(max_length=100, primary_key=True)  

    def __str__(self) -> str:
        return self.name     

class Question(models.Model):
    # question_text : 200 자 제한
    question_text = models.CharField(max_length=200,verbose_name="질문")
    # pub_date : 시간,날짜
    pub_date = models.DateTimeField(verbose_name="작성날짜")

    # str : question_text 리턴
    def __str__(self) -> str:
        return self.question_text

class Choice(models.Model):
    # question = models.ForeignKey(Question,on_delete=models.CASCADE,verbose_name="the related Question")

    # choice_text : 200자 제한
    choice_text = models.CharField(max_length=200)
    # votes : 정수 값, default = 0
    votes = models.IntegerField(default=0,verbose_name="투표")

    # str : choice_text 리턴
    def __str__(self) -> str:
        return self.choice_text