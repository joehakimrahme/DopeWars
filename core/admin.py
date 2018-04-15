from django.contrib import admin

# Register your models here.
from .models import Item, Game

admin.site.register(Item)
admin.site.register(Game)
