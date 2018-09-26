from django.contrib import admin
from .models import BookName, BlogTag
# Register your models here.

@admin.register(BookName)
class BookNameAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_time','update_time')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'slug','body_level','body_page','body_parent','bookname','created_time','update_time')
