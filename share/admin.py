from django.contrib import admin
from .models import ShareModel, ShareOwnershipModel


admin.site.register(ShareModel)
admin.site.register(ShareOwnershipModel)

