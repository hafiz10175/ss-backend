from django.db import models
from django.db.models import Q


class NoteQuerySet(models.QuerySet):
    def filter_by_user(self, user):
        q = Q()
        if user.is_superuser:
            return self.filter(q)
        else:
            q &= Q(created_by=user)
            return self.filter(q)


class NoteManager(models.Manager):
    def get_queryset(self):
        return NoteQuerySet(self.model, using=self._db)

    def filter_by_user(self, user):
        return super().get_queryset().filter_by_user(user)
