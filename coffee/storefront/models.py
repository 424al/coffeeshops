from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from uuid import uuid4

# List that determines whether or not shop get's approved to be displayed

ACTIVE =(
	(0, "NOT APPROVED"),
	(1, "APPROVED"),
    )



class UserManager(BaseUserManager):

  def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
    if not email:
        raise ValueError('Users must have an email address')
    now = timezone.now()
    email = self.normalize_email(email)
    user = self.model(
        email=email,
        is_staff=is_staff,
        is_active=True,
        is_superuser=is_superuser,
        last_login=now,
        date_joined=now,
        **extra_fields
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, password, **extra_fields):
    return self._create_user(email, password, False, False, **extra_fields)

  def create_superuser(self, email, password, **extra_fields):
    user=self._create_user(email, password, True, True, **extra_fields)
    user.save(using=self._db)
    return user





class User(AbstractBaseUser, PermissionsMixin):
      email = models.EmailField(max_length=254, unique=True)
      name = models.CharField(max_length=254, null=True, blank=True)
      is_staff = models.BooleanField(default=False)
      is_superuser = models.BooleanField(default=False)
      is_active = models.BooleanField(default=True)
      last_login = models.DateTimeField(null=True, blank=True)
      date_joined = models.DateTimeField(auto_now_add=True)

      USERNAME_FIELD = 'email'
      EMAIL_FIELD = 'email'
      REQUIRED_FIELDS = []

      objects = UserManager()

      def get_absolute_url(self):
          return "/users/%i/" % (self.pk)


class StoreFront(models.Model):
    uuid = models.UUIDField(primary_key=False, default=uuid4, editable=False)
    name = models.CharField(max_length=250, blank=False)
    street_address = models.CharField(max_length=100, blank=True)
    additional_address_field = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=100, blank=False)
    latitude = models.FloatField(blank=False,default=0.0)
    longitude = models.FloatField(blank=False,default=0.0)
    phone = models.CharField(max_length=100, blank=True)
    instagram_username =models.CharField(max_length=100, blank=True)
    status = models.IntegerField(choices=ACTIVE, default=0)
    created_by = models.ForeignKey(
        User,
        related_name="location_made_by",
        on_delete=models.SET_NULL,
        null=True,
    )


    """
    Fix items below in future branch
    """
    # created_by =
    # lattitude =
    # longitude =
    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name


