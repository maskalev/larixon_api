from django.contrib import admin
from django.contrib.admin.filters import DateFieldListFilter

from .models import Advert, Category, City


class AdvertAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "city", "category", "views", "created")
    readonly_fields = ("views",)
    list_filter = ("city", "category", ("created", DateFieldListFilter))
    search_fields = ("title", "description")


admin.site.register(Category)
admin.site.register(City)
admin.site.register(Advert, AdvertAdmin)
