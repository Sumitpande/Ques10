from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
    # list_display = ['name', 'slug']
    # prepopulated_fields = {'slug': ('name',)}

@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    pass
    # list_display = ['id','name', 'slug', 'price',
    # 'available', 'created', 'updated']
    # list_filter = ['available', 'created', 'updated']
    # list_editable = ['price', 'available']
    # prepopulated_fields = {'slug': ('name',)}