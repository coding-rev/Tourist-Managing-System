# Python/Django imports
from django.db import models
import uuid
# Local app import
from tms.basemodels import TimeBaseModel
from .site import Site
from tourist.models.tourist import Tourist

class Payment(TimeBaseModel):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tourist     = models.ForeignKey(Tourist, on_delete=models.CASCADE)
    site        = models.ForeignKey(Site, on_delete=models.SET_NULL, null=True, blank=True)
    amount_paid = models.FloatField(default=0.0)
    date        = models.DateField(auto_now=True)


    def __str__(self):
        return f"{self.tourist.first_name} {self.tourist.last_name} payment for {self.site.name}"


