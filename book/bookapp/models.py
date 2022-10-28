from django.db import models

### Book(code,title,author,price,register_dttm)
# code(정수 값, pk 지정),title(문자, 200),author(문자, 50),price(정수),register_dttm(날짜,시간)
# 테이블 이름 : bookTBL

class Book(models.Model):
    code = models.IntegerField(primary_key=True, verbose_name="코드")
    title = models.CharField(max_length=200, verbose_name="제목")
    author = models.CharField(max_length=50, verbose_name="저자")
    price = models.IntegerField(verbose_name="가격")
    register_dttm = models.DateTimeField(auto_now_add=True, verbose_name="등록날짜")

    class Meta:
        db_table = "bookTBL"

    def __str__(self) -> str:
        return self.title

