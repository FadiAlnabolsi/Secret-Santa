from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from .models import SecretSantaGroup, assignment, UserInfo, Item

# Register your models here.

admin.site.register(SecretSantaGroup)
admin.site.register(assignment)
admin.site.register(Item)

class User_Info(admin.StackedInline):
	model = UserInfo
	can_delete = False
	verbose_name_plural = 'User_Info'

class UserAdmin(UserAdmin):
	inlines = (User_Info, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
