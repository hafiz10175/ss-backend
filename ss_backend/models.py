from django.db import models


# base model
class BaseModel(models.Model):
    # add a created_at field
    created_at = models.DateTimeField(auto_now_add=True)
    # add an updated_at field
    updated_at = models.DateTimeField(auto_now=True)

    # add a Meta class to define the abstract model
    class Meta:
        abstract = True
