from django.contrib import admin

from main.models import Address


class AddressAdmin(admin.ModelAdmin):
    ...


admin.site.register(Address, AddressAdmin)
