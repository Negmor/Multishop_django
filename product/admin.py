from django.contrib import admin
from . import models


# Register your models here.


class InformationAdmin(admin.StackedInline):
    model = models.Information


@admin.register(models.Category)
class Category(admin.ModelAdmin):
    list_display = ("slug","title","parent")
    prepopulated_fields = {"slug":("title",)}



@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("price", "title")
    inlines = (InformationAdmin,)


admin.site.register(models.Color)
admin.site.register(models.Size)
