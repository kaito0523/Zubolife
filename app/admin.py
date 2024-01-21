from django.contrib import admin
from .models import Recipe,Memo
from accounts.models import CustomUser
# Register your models here.

admin.site.register(Recipe)
admin.site.register(CustomUser)
admin.site.register(Memo)
