from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from import_export import resources
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from import_export.admin import ImportExportActionModelAdmin
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

from .models import (
    Stuff,
    Device,
    Brand,
    Category,
    Observation,
    Action,
    Reasoning,
    Intervention,
    RepairFolder,
    Status,
)

ENCODING = 'ISO_LATIN_1'

class DeviceAdmin(DynamicArrayMixin, ImportExportActionModelAdmin, SimpleHistoryAdmin):
    to_encoding = ENCODING
    from_encoding = ENCODING
    
    class Meta:
        model = Device


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category


class CategoryAdmin(ImportExportActionModelAdmin, TreeAdmin):
    to_encoding = ENCODING
    from_encoding = ENCODING
    form = movenodeform_factory(Category)


class BrandAdmin(ImportExportActionModelAdmin, SimpleHistoryAdmin):
    to_encoding = ENCODING
    from_encoding = ENCODING
    ... 

class ObservationAdmin(ImportExportActionModelAdmin, SimpleHistoryAdmin):
    to_encoding = ENCODING
    from_encoding = ENCODING
    ... 

class ActionAdmin(ImportExportActionModelAdmin, SimpleHistoryAdmin):
    to_encoding = ENCODING
    from_encoding = ENCODING
    ... 

class ReasoningAdmin(ImportExportActionModelAdmin, SimpleHistoryAdmin):
    to_encoding = ENCODING
    from_encoding = ENCODING
    ... 

class StatusAdmin(ImportExportActionModelAdmin, SimpleHistoryAdmin):
    to_encoding = ENCODING
    from_encoding = ENCODING
    ... 

admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Stuff, SimpleHistoryAdmin)
admin.site.register(Observation,ObservationAdmin)
admin.site.register(Action, ActionAdmin)
admin.site.register(Reasoning, ReasoningAdmin)
admin.site.register(Intervention, SimpleHistoryAdmin)
admin.site.register(RepairFolder, SimpleHistoryAdmin)
admin.site.register(Status, StatusAdmin)
