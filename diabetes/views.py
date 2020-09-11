from django.shortcuts import render, redirect
import pandas as pd
from .models import DiabeticPrediction


# Create your views here.


def predict(request):
    if request.method == 'POST':
        Name = request.POST['Name']
        Glucose = request.POST['Glucose']
        BloodPressure = request.POST['BloodPressure']
        SkinThickness = request.POST['SkinThickness']
        Insulin = request.POST['Insulin']
        BMI = request.POST['BMI']
        Age = request.POST['Age']
        model = pd.read_pickle('diabetespredict.pickle')
        result = model.predict(
            [[Glucose, BloodPressure, SkinThickness, Insulin,
              BMI, Age]])  # input must be 2D array
        print(result)
        is_diabetic = result[0]
        ins = DiabeticPrediction(Glucose=Glucose, BloodPressure=BloodPressure, SkinThickness=SkinThickness,
                                 Insulin=Insulin, Name=Name,
                                 BMI=BMI, Age=Age, is_diabetic=is_diabetic)
        ins.save()
        context = {'Glucose': Glucose, 'BloodPressure': BloodPressure, 'SkinThickness': SkinThickness,
                   'Insulin': Insulin, 'final': is_diabetic,
                   'BMI': BMI, 'Age': Age}
        return render(request, 'index.html', context)
    return render(request, 'index.html')


def results(request):
    preds = DiabeticPrediction.objects.all()
    context = {'preds': preds}
    return render(request, 'results.html', context)


def delete(request):
    predss = DiabeticPrediction.objects.all()
    predss.delete()
    return redirect('/')
