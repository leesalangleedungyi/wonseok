from django.db import models

# 데이터베이스 작업
# 테이블 == 클래스로 작업

# Photo
# 컬럼 : pk,제목,저작자,이미지,사진설명,가격
# 데이터 타입 : 숫자,문자열,문자열,문자열(이미지주소),문자열,숫자

# 문자열 : CharField(max_length 지정 필요), TextField()
class Photo(models.Model):
    # 필드명 = 필드타입(조건......)
    # pk(장고에서 기본적으로 생성- 단순 숫자 증가)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    image = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self) -> str:
        return self.title + " " + self.author