from django.contrib import admin
from staple.models import Document

# Register your models here.
class DocumentAdmin(admin.ModelAdmin):
    """ Show helpful fields on the changelist page. """
    list_display = ('title', 'slug', 'author', 'created', 'modified')

admin.site.register(Document, DocumentAdmin)