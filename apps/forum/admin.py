from django.contrib import admin

# Register your models here.

from .models import Category, Topic, Reply, Profile

models = (Category, Topic, Reply)

admin.site.register(models)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("username",)
    search_fields = ["user__username"]