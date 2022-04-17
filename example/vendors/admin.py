from django.contrib import admin

from .models import Vendor, VendorUser, VendorOwner


admin.site.register(Vendor)



admin.site.register(VendorUser)
admin.site.unregister(VendorUser)

@admin.register(VendorUser)
class CustomVendor(admin.ModelAdmin):
    list_display = ["user", "organization", "is_admin"]
    raw_id_fields = ("user", "organization")

admin.site.register(VendorOwner)
