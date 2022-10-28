from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver


# 이메일, 성명, 사용자이름, 비밀번호 컬럼으로 User 생성

# Manager
class AlpagramManager(BaseUserManager):
    def _create_user(self, email, name, nickname, password, **extra_fields):

        if not email:
            raise ValueError("The given email must be set")

        email = self.normalize_email(email)                       
        user = self.model(email=email, name=name, nickname=nickname,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, name, nickname, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, name, nickname, password, **extra_fields)

    def create_superuser(self, email, name, nickname, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, name, nickname, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    AbstractBaseUser : User 를 생성할 수 있는 추상 클래스
    """

    email = models.EmailField(verbose_name="이메일", unique=True, max_length=128)
    name = models.CharField(verbose_name="이름", max_length=50)
    nickname = models.CharField(verbose_name="사용자 이름", max_length=50)

    is_staff = models.BooleanField(default=False)

    objects = AlpagramManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name","nickname"]

    class Meta:
        db_table = "alpagram_user"


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, verbose_name="회원")
    image = models.ImageField(upload_to = "profile/", default="profile/default.png")
    

    class Meta:
        db_table = "alpagram_user_profile"

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)