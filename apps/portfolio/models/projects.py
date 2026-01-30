from django.db import models

from apps.base.models.base_model import BaseModel


class ProjectCategory(BaseModel):
    name = models.CharField(max_length=255, verbose_name="Category Name", unique=True)

    class Meta:
        verbose_name = "Project Category"
        verbose_name_plural = "Project Categories"

    def __str__(self):
        return self.name


class ProjectTechnology(BaseModel):
    name = models.CharField(max_length=255, verbose_name="Technology Name", unique=True)

    class Meta:
        verbose_name = "Project Technology"
        verbose_name_plural = "Project Technologies"

    def __str__(self):
        return self.name


class Project(BaseModel):
    title = models.CharField(max_length=255, verbose_name="Project Title")
    category = models.ForeignKey(
        ProjectCategory, on_delete=models.PROTECT, verbose_name="Project Category"
    )
    customer_name = models.CharField(max_length=255, verbose_name="Customer Name")
    short_description = models.TextField(verbose_name="Short Description")
    long_description = models.TextField(verbose_name="Long Description")
    cover_image = models.ImageField(
        upload_to="projects/covers/", verbose_name="Cover Image"
    )
    is_featured = models.BooleanField(default=True, verbose_name="Is Featured")
    technologies = models.ManyToManyField(
        ProjectTechnology, verbose_name="Technologies Used"
    )
    started_at = models.DateField(verbose_name="Start Date")
    ended_at = models.DateField(null=True, blank=True, verbose_name="End Date")
    live_url = models.URLField(null=True, blank=True, verbose_name="Live URL")
    repo_url = models.URLField(null=True, blank=True, verbose_name="Repository URL")
