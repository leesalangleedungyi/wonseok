from django.db import models

from users.models import CustomUser

from taggit.managers import TaggableManager

# 테이블명 alpaco_board
# Board - title(128), contents(TextField), writer(CustomUser), created_at, tags
class Board(models.Model):
    title = models.CharField(max_length=128, verbose_name="제목")
    contents = models.TextField()
    writer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="작성자")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="등록날짜")
    tags = TaggableManager(blank=True)

    class Meta:
        db_table = 'alpaco_board'