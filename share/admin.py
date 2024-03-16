from django.contrib import admin
from .models import *

admin.site.register(ShareModel)
admin.site.register(ShareOwnershipModel)
admin.site.register(SlotModel)
admin.site.register(PublicOfferingModel)
admin.site.register(PasswordResetModel)
