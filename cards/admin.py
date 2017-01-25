from django.contrib import admin

from .models import Card


class CardAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'is_title_visible',
                    'text',
                    'author',
                    'is_active')


admin.site.register(Card, CardAdmin)
