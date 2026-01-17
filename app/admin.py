from django.contrib import admin
from app.models import Report
# Register your models here.
@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display=("id","name","email","source","date1")
    search_fields=("name","email")
    list_filter=("name","message")
    ordering=("-id",)
    actions=["deleted_selected"]