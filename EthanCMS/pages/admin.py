from django.contrib import admin
from pages.models import Tag, Page

admin.site.register(Tag)

class PageAdmin(admin.ModelAdmin):
    exclude = ("body_html",)
    readonly_fields = ("url",)

admin.site.register(Page, PageAdmin)