# 🎓 Student Performance Prediction using Machine Learning

An end-to-end Machine Learning web application built with **Python, Scikit-learn, Django, HTML, and CSS** that predicts a student's Performance Index based on study-related factors.

---

## 📌 Project Overview

This project uses a **Linear Regression** model to predict the **Performance Index** of a student based on the following features:

* 📚 Hours Studied
* 📝 Previous Scores
* ⚽ Extracurricular Activities
* 🌙 Sleep Hours
* 📄 Sample Question Papers Practiced

The trained model is integrated into a **Django web application**, allowing users to enter student details and receive predictions through a clean web interface.

---

## 🚀 Features

* Data Cleaning and Preprocessing
* Exploratory Data Analysis (EDA)
* Feature Encoding
* Model Training using Linear Regression
* Decision Tree Comparison
* Cross Validation
* Hyperparameter Tuning
* Model Serialization using Joblib
* Django Web Application
* Responsive HTML & CSS User Interface

---

## 🛠️ Tech Stack

### Machine Learning

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib

### Web Development

* Django
* HTML5
* CSS3

### Development Tools

* Jupyter Notebook
* VS Code
* Git
* GitHub

---

## 📂 Project Structure

```text
Student_Score_Prediction/
│
├── app/
├── predictor/
├── data/
├── models/
│   └── linear_regression.pkl
├── notebooks/
├── reports/
├── src/
├── static/
│   └── css/
├── templates/
│   └── index.html
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📊 Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Engineering
5. Train-Test Split
6. Model Training
7. Model Evaluation
8. Hyperparameter Tuning
9. Model Saving
10. Django Integration
11. Prediction through Web Interface

---

## 📈 Model Performance

| Metric   | Value     |
| -------- | --------- |
| MAE      | **1.61**  |
| MSE      | **4.08**  |
| RMSE     | **2.02**  |
| R² Score | **0.989** |

The Linear Regression model achieved an **R² Score of approximately 98.9%**, indicating excellent predictive performance on the dataset.

---

## 🖥️ How to Run the Project

### 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Student_Score_Prediction.git
```

### 2. Open Project

```bash
cd Student_Score_Prediction
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Django Server

```bash
python manage.py runserver
```

### 5. Open Browser

```
http://127.0.0.1:8000/
```

---

## 📷 Application Preview

Add screenshots here after uploading them.

```
Home Page Screenshot

Prediction Result Screenshot
```

---

## 📚 What I Learned

Through this project, I learned:

* Machine Learning Workflow
* Data Cleaning and Preprocessing
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Regression Algorithms
* Model Evaluation Metrics
* Cross Validation
* Hyperparameter Tuning
* Model Serialization
* Django Integration with Machine Learning
* Building End-to-End ML Applications

---

## 🔮 Future Improvements

* Random Forest Regression
* XGBoost
* Model Explainability
* User Authentication
* Prediction History
* Cloud Deployment
* Docker Support
* REST API using Django REST Framework

---

## 👨‍💻 Author

**Devendra Yadav**

B.Tech Computer Science (Data Science)

Passionate about Machine Learning, Artificial Intelligence, and Full Stack Development.

GitHub: https://github.com/Devendra470

LinkedIn: www.linkedin.com/in/devendra-singh-yadav-a952892a7

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

It motivates me to build more Machine Learning projects.
