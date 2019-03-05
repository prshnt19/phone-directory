from django.contrib import admin
from .models import PhoneDirectory

# Register your models here.


class PhoneDirectoryEntry(admin.ModelAdmin):
    List_display = ("id", "name", "number")


admin.site.register(PhoneDirectory, PhoneDirectoryEntry)