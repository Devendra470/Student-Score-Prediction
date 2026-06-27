from django.shortcuts import render
import joblib
import pandas as pd

model=joblib.load(r"models\linear_regression.pkl")
# Create your views here.
def home(request):
    prediction=None
    if(request.method=="POST"):
        print(request.POST)
        hours=float(request.POST['hours'])
        previous=float(request.POST['previous'])
        activities = request.POST["activities"]
        sleep = float(request.POST["sleep"])
        papers = float(request.POST["papers"])
        activities=1 if activities=="Yes" else 0
        data = pd.DataFrame({

            "Hours Studied":[hours],

            "Previous Scores":[previous],

            "Extracurricular Activities":[activities],

            "Sleep Hours":[sleep],

            "Sample Question Papers Practiced":[papers]

        })
        prediction=model.predict(data)[0]
    return render(request,'index.html',{"prediction":prediction})

