from django.contrib import admin

from .models import Card


class CardAdmin(admin.ModelAdmin):
    list_display = ('text',
                    'secondary_text',
                    'is_active',
                    'update_datetime',
                    'updated_by',
                    'creation_datetime',
                    'created_by')


admin.site.register(Card, CardAdmin)
