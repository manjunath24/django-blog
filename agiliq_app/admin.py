from django.contrib import admin
from agiliq_app.models import Article, Comment

class AuthorAdmin(admin.ModelAdmin):
    exclude = ('slug',)

admin.site.register(Article, AuthorAdmin)
admin.site.register(Comment)

# Register your models here.
