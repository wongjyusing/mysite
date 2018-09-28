from django.contrib import admin
from .models import MySiteData,Home,About,FriendLink,SpaceLink,BookLink
# Register your models here.
@admin.register(MySiteData)
class MySiteDataAdmin(admin.ModelAdmin):
    list_display = ('logo', 'introduction', 'source_of_power','approval_number')

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_time','update_time')

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_time','update_time')


@admin.register(FriendLink)
class FriendLinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')

@admin.register(SpaceLink)
class SpaceLinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')

@admin.register(BookLink)
class BookLinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')
