from django.contrib import admin
from .models.payment import Payment
from .models.site import Site

admin.site.register(Payment)
admin.site.register(Site)
