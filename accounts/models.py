from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):

    first_name = None
    last_name = None

    name = models.CharField(max_length=16)
    email = models.EmailField(max_length=128, blank=False, null=False, unique=True)
    username = models.CharField(max_length=64, blank=False, null=False, unique=True)
    update_date = models.DateTimeField(auto_now=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "auth_user"

    def __str__(self):
        return f"{str(self.pk)}:\t{str(self.name)}"


class ClassBase(models.Model):
    STATUS = (
        (0, "Inactive"),
        (1, "Active"),
    )

    is_active = models.IntegerField(choices=STATUS, default=1)
    insert_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Images(ClassBase):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True)

    class Meta:
        db_table = "tbl_image"
