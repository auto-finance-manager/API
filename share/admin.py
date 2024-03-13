from django.contrib import admin
from .models import ShareModel, ShareOwnershipModel, SlotModel, PublicOfferingModel

admin.site.register(ShareModel)
admin.site.register(ShareOwnershipModel)
admin.site.register(SlotModel)
admin.site.register(PublicOfferingModel)
    