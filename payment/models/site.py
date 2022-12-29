# Python/Django imports
from django.db import models
import uuid
# Local app import
from tms.basemodels import TimeBaseModel

class Site(TimeBaseModel):
    id    = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name  = models.CharField(max_length=100)      

    def __str__(self):
        return self.name

