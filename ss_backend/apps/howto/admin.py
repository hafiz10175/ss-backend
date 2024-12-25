from django.contrib import admin
from .models import Note, NoteCategory, NoteTag

# Register your models here.

admin.site.register(NoteCategory)
admin.site.register(NoteTag)


class NoteAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "status", "created_at", "updated_at")
    list_filter = ("category", "status", "created_at", "updated_at")
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}

    class Meta:
        model = Note

admin.site.register(Note, NoteAdmin)
