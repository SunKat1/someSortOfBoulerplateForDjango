from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
  def create_user(self, email, password=None):
    if not email:
      raise ValueError("User must have an email")

    user = self.model(
      email = self.normalize_email(email),
    )

    user.set_password(password)
    user.save(using = self._db)

    return user

  def create_superuser(self, email, password):
    user = self.create_user(
      email = self.normalize_email(email),
      password = password
    )
    user.is_admin = True
    user.is_staff = True
    user.is_superuser = True
    user.save(using = self._db)

    return user

class UserAccount(AbstractBaseUser):
  ROLES_LIST = [
    ('admin', 'admin'),
    ('guest', 'guest'),
    ('delivery', 'delivery'),
    ('sales', 'sales')
  ]

  email = models.EmailField(verbose_name='email', max_length=60, unique=True)
  username = models.CharField(max_length=30, unique=True, blank=True)
  role = models.CharField(choices=ROLES_LIST, default='guest', blank=True, max_length=100)
  avatar = models.ImageField(verbose_name='avatar', blank=True) 
  date_joined=models.DateTimeField(verbose_name='date_joined', auto_now_add=True)
  last_login = models.DateTimeField(verbose_name='last_login', auto_now=True)
  is_admin = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=True)
  is_superuser = models.BooleanField(default=False)

  USERNAME_FIELD = 'email'

  REQUIRED_FIELDS = []

  objects = UserManager()

  def __str__(self):
    return self.email

  def has_perm(self, permissions, obj=None):
    return self.is_admin
  
  def has_module_perms(self, app_label):
    return True