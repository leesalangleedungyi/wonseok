from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


# 회원가입 - 이메일, 이름, 전화번호, 비밀번호 필드만 사용한다고 할 때


# 매니저 생성
class AccountManager(BaseUserManager):
    def _create_user(self, email, name, phone, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)                       
        user = self.model(email=email, name=name, phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, name, phone, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, name, phone, password, **extra_fields)

    def create_superuser(self, email, name, phone, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, name, phone, password, **extra_fields)


# User class 생성
class CustomUser(AbstractBaseUser, PermissionsMixin):
    # 이메일을 userid 로 사용
    email = models.EmailField(verbose_name ="이메일", unique=True)
    name = models.CharField(verbose_name ="이름",max_length=50)
    phone = models.CharField(verbose_name ="핸드폰",max_length=50)

    is_staff = models.BooleanField(default=False)

    objects = AccountManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name','phone']

    class Meta:
        db_table = "alpaco_user"