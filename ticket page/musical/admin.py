from django.contrib import admin
from musical.models import Musical

@admin.register(Musical)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id','title','description')
