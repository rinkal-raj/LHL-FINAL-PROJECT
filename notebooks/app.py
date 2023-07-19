from flask import render_template, request, jsonify,Flask
import flask
import numpy as np
import traceback #allows you to send error to user
import pickle
import pandas as pd
import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)


# App definition
app = Flask(__name__)

# importing models
with open('log_reg.pkl', 'rb') as f:
   log_reg = pickle.load(f)

with open('model_columns.pkl', 'rb') as f:
   model_columns = pickle.load(f)

#webpage

@app.route('/')
def welcome():
   return "Welcome! Use this Flask App for Heart Diseases Prediction"

@app.route('/predict', methods=['POST','GET'])
def predict():

   if flask.request.method == 'GET':
       print("we are inside the GET method!")
       return "Prediction page. Try using post with params to get specific prediction."

   if flask.request.method == 'POST':
       try:
           json_ = request.json # '_' since 'json' is a special word
           print(json_)
           query_ = pd.get_dummies(pd.DataFrame(json_))
           query = query_.reindex(columns = model_columns, fill_value= 0)
           print("[0] Patient does not have Heart Dieases")
           print("[1] Patient has Heart Dieases")
           #print("Query:", query)

           prediction = list(log_reg.predict(query))
           result = "Patient does not have heart disease"
           if prediction[0] == 1:
               result = "Patient has heart disease"


           return jsonify({
              "Prediction": str(prediction),
              "Result": result
           })

       except:
           return jsonify({
               "trace": traceback.format_exc()
               })



if __name__ == "__main__":
   app.run()
