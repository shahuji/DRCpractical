from django.contrib import admin

from .models import Images

from django.contrib.auth import get_user_model


User = get_user_model()

# Register your models here.


class ImagesListInline(admin.TabularInline):
    model = Images


class UserAdmin(admin.ModelAdmin):
    inlines = [ImagesListInline, ]


admin.site.register(User, UserAdmin)