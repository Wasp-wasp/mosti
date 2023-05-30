from django.contrib import admin

# Register your models here.
from shop.models import Bridge, User


class ObjectAdmin(admin.ModelAdmin):
    list_display = ('id_object', 'name_object')




admin.site.register(Bridge, ObjectAdmin)
admin.site.register(User)
