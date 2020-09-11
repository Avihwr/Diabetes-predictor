from django.db import models


# Create your models here.


class DiabeticPrediction(models.Model):
    Name = models.CharField(max_length=50)
    Glucose = models.FloatField()
    BloodPressure = models.FloatField()
    SkinThickness = models.FloatField()
    Insulin = models.FloatField()
    BMI = models.FloatField()
    Age = models.PositiveIntegerField()
    is_diabetic = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.Name
