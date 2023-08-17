from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin



# Register your models here.
admin.site.register(Receipts)
admin.site.register(Register)

#this add the import export model to the admin
@admin.register(Pledges)
class PledgesAdmin(ImportExportModelAdmin):
    pass