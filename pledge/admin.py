from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin



# Register your models here.
@admin.register(Receipts)
class ReceiptsAdmin(ImportExportModelAdmin):
    pass


#this add the import export model to the admin
@admin.register(Pledges)
class PledgesAdmin(ImportExportModelAdmin):
    pass


@admin.register(Register)
class RegisterAdmin(ImportExportModelAdmin):
    pass