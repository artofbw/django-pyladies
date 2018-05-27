from django.contrib import admin

from .models import TvStation, TvProgram

# Register your models here.
@admin.register(TvStation)
class TvStationAdmin(admin.ModelAdmin):
    pass


@admin.register(TvProgram)
class TvProgramAdmin(admin.ModelAdmin):
    pass