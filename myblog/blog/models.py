from django.db import models
from user.models import User

from taggit.managers import TaggableManager


# 글번호(자동-pk), 제목(30), 내용(TextField), 작성날짜(DateTime), 수정날짜, 작성자(User),
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, blank=False)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True)
    # auto_now_add : (생성일자) - 최초 저장시만 현재날짜 삽입 
    # auto_now : (수정일자) - 갱신될 때마다 날짜 삽입
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    # 좋아요
    likes = models.ManyToManyField(User,related_name="likes",blank=True)

    # tag
    tags = TaggableManager(blank=True)

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    """
    댓글 - 글번호(자동-pk), 내용(TextField), 작성날짜(DateTime), 수정날짜, 작성자(User), post글번호
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return "%s - %s" % (self.id, self.user)