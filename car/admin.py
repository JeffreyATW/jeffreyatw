from jeffreyatw.car.models import Character, Comic, Comment
from django.contrib import admin

class CommentAdmin(admin.ModelAdmin):
    fields = ['name', 'website', 'content']
    list_display = ('name', 'content', 'pub_date')

admin.site.register(Comic)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Character)
