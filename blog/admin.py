from django.contrib import admin
from .models import Contactus,Post,Emails
# Register your models here.
admin.site.register((Contactus,Emails))


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)