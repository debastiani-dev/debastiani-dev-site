from typing import Any
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from apps.base.models import BaseModel, BaseManager


class UserManager(BaseUserManager, BaseManager):
    def create_user(
        self, email: str, first_name: str, last_name: str, password: str, **extra_fields
    ) -> "User":
        if not email:
            raise ValueError(_("Users must have an email address"))

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, email: str, first_name: str, last_name: str, password: str, **extra_fields
    ) -> "User":
        user = self.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            **extra_fields,
        )
        user.is_admin = True
        user.is_superuser = True  # Provided by PermissionsMixin
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    email = models.EmailField(_("Email"), max_length=255, unique=True, db_index=True)
    first_name = models.CharField(_("First name"), max_length=50)
    last_name = models.CharField(_("Last name"), max_length=50)
    phone_number = PhoneNumberField(
        _("Phone number"), null=True, blank=True, unique=False
    )
    is_active = models.BooleanField(_("Active"), default=True)
    is_admin = models.BooleanField(_("Admin"), default=False)
    photo = models.ImageField(_("Photo"), upload_to="avatars/", null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self) -> str:
        return f"{self.email} ({self.pk})"

    @property
    def is_staff(self) -> bool:
        return self.is_admin

    @property
    def fullname(self) -> str:
        return f"{self.first_name.title()} {self.last_name.title()}"
