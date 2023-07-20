# LHL-FINAL-PROJECT

### Project/Goals
The objective of this project is to create various machine learning models and get a prediction about whether a patient has heart disease or not and also perform exploratory data analysis and create meaningful visualizations in tableau using the heart dataset. The project involved main stages: data preprocessing, analysis using Python, Flask application which predicts person has heart disease or not and visualization using Tableau. The ultimate goal was to gain insights and communicate findings regarding heart disease affects variables patterns, and other relevant aspects of the dataset.

### Process

### Step 1:  Data Collection:
The first step of the project involved selecting and downloading datasets from online. Downloaded heart dataset from the Kaggle website. The dataset included attributes such as 
Age: age of the patient [years]
Sex: sex of the patient [M: Male, F: Female]
ChestPainType: chest pain type [TA: Typical Angina, ATA: Atypical Angina, NAP: Non-Anginal Pain, ASY: Asymptomatic]
RestingBP: resting blood pressure [mm Hg]
Cholesterol: serum cholesterol [mm/dl]
FastingBS: fasting blood sugar [1: if FastingBS > 120 mg/dl, 0: otherwise]
RestingECG: resting electrocardiogram results [Normal: Normal, ST: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV), LVH: showing probable or definite left ventricular hypertrophy by Estes' criteria]
MaxHR: maximum heart rate achieved [Numeric value between 60 and 202]
ExerciseAngina: exercise-induced angina [Y: Yes, N: No]
Oldpeak: oldpeak = ST [Numeric value measured in depression]
ST_Slope: the slope of the peak exercise ST segment [Up upsloping, Flat: flat, Down: downsloping]
HeartDisease: output class [1: heart disease, 0: Normal]

   
### Step 2 : Data Preprocessing:
To ensure data integrity and reliability, the raw dataset underwent preprocessing using Python. This step included handling missing values, transforming data types, and extracting relevant features. Additionally, data normalization, and data scaling, data encoding techniques were applied to address any inconsistencies or anomalies in the dataset.

### Step 3 : Exploratory Data Analysis (EDA):
After preprocessing the data, an exploratory data analysis was conducted to gain a deeper understanding of the dataset. This involved performing descriptive statistics, visualizing data distributions, and identifying patterns and trends within the heart data. EDA techniques such as histograms, scatter plots, bar charts, and heatmaps were utilized to explore relationships between variables and identify potential insights.

### Step 4 : Regression Modeling:
To find the relationship between variables and make predictions, a regression model was built. The model focused on the prediction of patients has heart diseases which variables play an important role. The multivariable regression model was implemented using Python's statsmodels library, and model evaluation metrics were analyzed to assess the model's performance.

### Step 5 : Machine Learning Models:
This is a more important part of a project using this classification model to predict patient has heart disease or not. Created more than 4 classification models and train that and found which model accuracy is the higher and use that model for the prediction of disease.

### Step 6 : Pickle:
Pickling is a process in Python that allows you to serialize (convert into a byte stream) Python objects and save them to a file. The serialized objects can later be deserialized (reconstructed) from the file back into Python objects. This process is useful for saving and loading complex data structures, machine learning models, and other Python objects.

### Step 7 : Flask Application:
The app uses a pre-trained machine learning model (Logistic Regression) to perform the heart disease prediction. The model has been trained on historical heart disease data to learn patterns and relationships between input features and the presence of heart disease. In this app, we can enter the patient's details, such as age, sex, blood pressure, cholesterol level, and other relevant medical information in json data and  get a prediction of a patient having heart disease based on the provided information.

### Step 8 : Tableau Visualization:
To effectively communicate the findings and provide an interactive visual experience, Tableau was used for data visualization. Various types of visualizations were created, including pie charts, bar charts, and scatter plots.

### Step 9 : Streamlit Application:
It is a web-based data application framework that allows to create interactive and data-driven applications using simple Python scripts.
Using this application I create heart predication application which is user friendly and take input from the user and give predication about diseases.

### Results
Through the systematic process of data preprocessing, exploratory analysis, regression modeling, visualization using Python and Tableau, and machine learning models this project successfully uncovered valuable insights into the heart dataset. Through the using Flask app we can enter details of a patient and easily predict patient has heart disease or not.

### Challenges
Throughout the project, I faced several challenges that required careful problem-solving and adaptability. Some of the main challenges I encountered are as follows:

Medical terminology word : The dataset contained some medical terminology words thus, it is difficult to understand the meaning of the word. Such as, RestingECG, ST_slope and many more.

Choosing Suitable EDA Techniques : The dataset comprised diverse attributes, making it challenging to determine the most suitable exploratory data analysis (EDA) techniques and also visualization in Tableau.

Building Classification Model: The process of model building and training was the most challenging part of the project because, during the time of model building one attribute of the dataset dropped thus, the model did not give proper output and error. And also, converting categorical data to numeric data it is more challenging for me.

Running Isuue with Flask App :  Flask Application was not properly run in a virtual environment due to some version setup issues in the Anaconda prompt and then after, installing all Python libraries in the command prompt after that, the application is working properly.
Before day of presentation , it is not working properly.

### Future Goals
If I have more time, I would like to create more classification models and compare the accuracy and find the best-fit model for the prediction of heart diseases.

Create a user-friendly Flask application in which the user adds data manually and finds the result of the prediction.

Generate more tableau visualization which makes it easy to user understand the dataset and a more interactive dashboard.
