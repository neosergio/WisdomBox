from django.contrib import admin

from .models import Card


class CardAdmin(admin.ModelAdmin):
    list_display = ('text', 'secondary_text', 'update_datetime', 'creation_datetime', 'created_by')

admin.site.register(Card, CardAdmin)
