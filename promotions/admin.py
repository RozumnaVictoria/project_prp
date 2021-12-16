from django.contrib import admin
from promotions.models import Promotions


@admin.register(Promotions)
class PromotionsAdmin(admin.ModelAdmin):
    fields = ['name', 'title', 'description', 'end', 'image']
