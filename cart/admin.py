from django.contrib import admin

# Register your models here.


from . import models

class orderItem(admin.TabularInline):
    model=models.OrderItem



@admin.register(models.Order)
class orderAdmin(admin.ModelAdmin):
    list_display = ("user","is_paid")
    inlines = (orderItem,)
    list_filter = ("is_paid",)


admin.site.register(models.DiscountModel)