from django.contrib import admin
from pdfs.models import PDF


class PDFAdmin(admin.ModelAdmin):
    list_display = ('issue', 'cover_story', 'pub_date')


admin.site.register(PDF, PDFAdmin)
