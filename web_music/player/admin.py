from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'id')


class SongAdmin(admin.ModelAdmin):
    list_display = ('user', 'song', 'id')


class PlayListAdmin(admin.ModelAdmin):
    list_display = ('user', 'play_list', 'songs_link')


admin.site.register(Songs, SongAdmin)
admin.site.register(Profile, UserAdmin)
admin.site.register(UserList, PlayListAdmin)
