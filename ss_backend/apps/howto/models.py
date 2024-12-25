from django.contrib.auth import get_user_model

from ss_backend.apps.howto.managers import NoteManager
from ss_backend.models import BaseModel
from django.db import models

User = get_user_model()


class NoteCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "note_category"
        verbose_name = "Note Category"
        verbose_name_plural = "Note Categories"

    def __str__(self):
        return self.name


class NoteTag(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "note_tag"
        verbose_name = "Note Tag"
        verbose_name_plural = "Note Tags"

    def __str__(self):
        return self.name


class Note(BaseModel):
    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        PUBLISHED = "published", "Published"
        ARCHIVED = "archived", "Archived"
        Deprecated = "deprecated", "Deprecated" # similar as archived, but not shown in the list

    title = models.CharField(max_length=255, unique=True, db_index=True, verbose_name="Title", help_text="Title",
                             blank=False, null=False)
    slug = models.SlugField(max_length=255, unique=True)
    content = models.TextField()
    category = models.ForeignKey(NoteCategory, on_delete=models.PROTECT)
    tags = models.ManyToManyField(NoteTag, blank=True, related_name="notes", related_query_name="note")
    status = models.CharField(max_length=30, choices=Status.choices, default=Status.DRAFT)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="notes",
                                   related_query_name="note")

    objects = NoteManager()

    class Meta:
        db_table = "note"
        verbose_name = "Note"
        verbose_name_plural = "Notes"

    def __str__(self):
        return self.title
