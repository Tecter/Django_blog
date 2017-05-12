from django.contrib import admin
from .models import Blog, Tag, Category, Comment, Person


# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created', 'update', )


class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name',)


admin.site.register([Category, Tag, Comment])
admin.site.register(Blog, BlogAdmin)
admin.site.register(Person, PersonAdmin)
