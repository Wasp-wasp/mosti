from django.contrib import admin

# Register your models here.
from shop.models import Object, User


class ObjectAdmin(admin.ModelAdmin):
    list_display = ('id_object', 'name_object')




admin.site.register(Object, ObjectAdmin)
admin.site.register(User)
