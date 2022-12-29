from django.db import models
import uuid
from tms.basemodels import TimeBaseModel

class Tourist(TimeBaseModel):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)