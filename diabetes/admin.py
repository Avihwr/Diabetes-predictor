from django.contrib import admin
from .models import DiabeticPrediction


# Register your models here.
class DiabeticAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'Age', 'is_diabetic')


admin.site.register(DiabeticPrediction, DiabeticAdmin)
