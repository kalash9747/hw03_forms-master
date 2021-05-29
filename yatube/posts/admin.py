from django.contrib import admin

from .models import Group, Post


class PostAdmin(admin.ModelAdmin):
    # перечисляем поля, которые должны отображаться в админке
    list_display = ("pk", "text", "pub_date", "author", "group")
    # добавляем интерфейс для поиска по тексту постов
    search_fields = ("text",)
    # добавляем возможность фильтрации по дате
    list_filter = ("pub_date",)
    empty_value_display = "-пусто-"


class GroupAdmin(admin.ModelAdmin):
    # перечисляем поля, которые должны отображаться в админке
    list_display = ("pk", "title", "description")
    # добавляем возможность фильтрации по заголовку
    list_filter = ("title",)
    empty_value_display = "-пусто-"

# при регистрации модели Post источником конфигурации для неё назначаем класс
# PostAdmin


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
