## Python test file for flask to test locally
import requests as r
import pandas as pd
import json
import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)


base_url = 'http://127.0.0.1:5000/' #base url local host

json_data = [
    {
    "Age" : 50,
    "Sex" :  1,
    "ChestPainType" : 4,
    "RestingBP" : 3,
    "Cholesterol" : 289,
    "FastingBS" : 1,
    "RestingECG" : 2,
    "MaxHR" : 156,
    "ExerciseAngina" : 1,
    "Oldpeak" : 1,
    "ST_Slope" : 1,
    
    }
]



# Get Response
# response = r.get(base_url)
response = r.post(base_url + "predict", json = json_data)


if response.status_code == 200:
    print('...')
    print('request successful')
    print('...')
    print(response.json())
else:
    print(response.json())
    print('request failed')
