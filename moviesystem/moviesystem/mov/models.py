from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, e_mail, user_name=None, password=None, **extra_fields):
        if not e_mail:
            raise ValueError('Users must have an email address')

        user = self.model(
            e_mail=self.normalize_email(e_mail),
            user_name=user_name,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, e_mail, password=None, **extra_fields):
        extra_fields.setdefault('user_role', 'admin')
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(e_mail, password=password, **extra_fields)

class CustomUser(AbstractBaseUser):
    user_name = models.CharField(max_length=50, unique=True)
    e_mail = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    user_role = models.CharField(max_length=10, default='user')
    registration_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'e_mail'
    REQUIRED_FIELDS = ['user_name']

    def __str__(self):
        return self.e_mail

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
