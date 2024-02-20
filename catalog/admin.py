from django.contrib import admin
from .models import Work, Image

class ImageInline(admin.TabularInline):
    fields = ["image","image_type","image_file_name","image_url","image_notes",]
    model = Image
    extra = 1


class WorkAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["title", "work_type", "media", "work_date", "dims_height", "dims_width", "dims_depth", "price", "work_key" ]}),
        ("Addition Info", {"fields": ["description","notes", "inscription"], "classes": ["collapse"]}),
        ("Sale info", {"fields": ["sold_to","sold_date", "sale_price"],"classes":["collapse"]})
    ]
    inlines = [ImageInline]
    list_display = ["title","work_type","media","work_date","dimensions"]


admin.site.register(Work, WorkAdmin)
