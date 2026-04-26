from django.contrib import admin
from .models import Experience, Training, Achievement


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("role", "org", "period", "current")


@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ("title", "issuer")


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ("name", "year", "result")
