from django.contrib import admin
from .models import ShareModel, ShareOwnershipModel, SlotModel


admin.site.register(ShareModel)
admin.site.register(ShareOwnershipModel)
admin.site.register(SlotModel)
