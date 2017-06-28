from django.contrib import admin

from .models import post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title","update","timestamp",]
    list_display_links = ["update"]
    list_editable = ["title"]
    list_filter = ["update","timestamp"]
    class Meta():
        model=post

admin.site.register(post,PostModelAdmin)
