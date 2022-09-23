from pydoc import describe
from turtle import Turtle
from django.db import models

# Create your models here.


class Todo(models.Model):
    #제목 (charfield = 글자제한 있음)
    title = models.CharField(max_length=50)
    #설명 (textfield = 글자제한 없음)
    description = models.TextField()
    #날짜 (자동 날짜 적용)
    created = models.DateTimeField(auto_now_add=True)
    #성공 여부(불린형)
    complete = models.BooleanField(default=False)
    # 중요도
    important = models.BooleanField(default=False)
    
    def __str__(self) -> str :
        return self.title