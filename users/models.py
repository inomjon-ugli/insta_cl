from django.contrib.auth.models import AbstractUser
from django.db import models
from shared.models import BaseModel

ORDINARY_USER, MANAGER, ADMIN = ("ordinary_user", "manager", "admin")
VIA_EMAIL, VIA_PHONE = ("via_email","via_phone")
NEW, CODE_VERIFIED, DONE, PHOTO = ("new", "code_verified", "done", "photo")

class User(AbstractUser, BaseModel):
    USER_ROLES = (

        (ORDINARY_USER, ORDINARY_USER),
        (MANAGER, MANAGER),
        (ADMIN, ADMIN),

    )
    AUTH_TYPE_CHOICES = (
        (VIA_EMAIL, VIA_EMAIL),
        (VIA_PHONE, VIA_PHONE),
    )
    AUTH_STATUS = (
        (NEW, NEW),
        (CODE_VERIFIED, CODE_VERIFIED),
        (DONE, DONE),
        (PHOTO, PHOTO),
    )
    user_role = models.CharField(max_length=31, choices=USER_ROLES, default=ORDINARY_USER)
    AUTH_TYPE = models.CharField(max_length=31, choices=AUTH_TYPE_CHOICES)
    AUTH_STATUS = models.CharField(max_length=31, choices=AUTH_STATUS, default=NEW)
    email = models.EmailField(unique=True, blank=True, null=True)
    phone_number = models.CharField(max_length=13, null=True, blank=True, unique=True)
    photo = models.ImageField(upload_to="user_photos", null=True, blank=True,)

    def __str__(self):
        return self.username


