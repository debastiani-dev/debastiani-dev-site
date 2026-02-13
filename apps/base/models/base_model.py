import uuid
from typing import Any, Optional

from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseQuerySet(models.QuerySet):
    def delete(self, destroy: bool = False) -> tuple[int, dict[str, int]]:
        if not destroy:
            return (
                self.update(is_deleted=True),
                {"rows_updated": self.count()},
            )
        return super().delete()

    def soft_delete(self) -> int:
        return self.update(is_deleted=True)

    def restore(self) -> int:
        return self.update(is_deleted=False)


class BaseManager(models.Manager):
    def get_queryset(self) -> BaseQuerySet:
        return BaseQuerySet(self.model, using=self._db).filter(is_deleted=False)


class AllObjectsManager(models.Manager):
    def get_queryset(self) -> BaseQuerySet:
        return BaseQuerySet(self.model, using=self._db)


class TimestampsOnlyBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    modified_at = models.DateTimeField(auto_now=True, verbose_name=_("Modified at"))

    class Meta:
        abstract = True


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    modified_at = models.DateTimeField(auto_now=True, verbose_name=_("Modified at"))
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name=_("uuid"),
        db_index=True,
        primary_key=True,
    )
    is_deleted = models.BooleanField(default=False, db_index=True)

    objects = BaseManager()
    all_objects = AllObjectsManager()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        update_fields = kwargs.get("update_fields", None)
        if update_fields:
            update_fields.append("modified_at")
        kwargs["update_fields"] = update_fields
        super().save(*args, **kwargs)

    def delete(
        self,
        using: Optional[str] = None,
        keep_parents: bool = False,
        destroy: bool = False,
    ) -> Any:
        if not destroy:
            return self.soft_delete()
        return models.Model.delete(self, using=using, keep_parents=keep_parents)

    def soft_delete(self) -> None:
        self.is_deleted = True
        self.save()

    def restore(self) -> None:
        self.is_deleted = False
        self.save()

    @property
    def deleted_date(self):
        """Returns modified_at as deleted_date if the object is deleted"""
        return self.modified_at if self.is_deleted else None
