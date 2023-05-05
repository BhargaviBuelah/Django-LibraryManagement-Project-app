from django.contrib import admin
from libraryapp.models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):

    list_display=['bname','bdesc','bauthor','copies','price','cat','is_deleted']
    list_filter=['is_deleted','cat']
admin.site.register(Book,BookAdmin)
