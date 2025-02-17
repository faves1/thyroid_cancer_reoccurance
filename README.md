# **Thyroid Cancer Recurrence Prediction Model**

This project uses machine learning to predict the likelihood of recurrence in thyroid cancer patients based on various clinical and demographic factors. The model is built using **Random Forest** and optimized with **hyperparameter tuning** and **feature selection**. The model is deployed using **Streamlit** for easy access and user interaction.

## **Table of Contents**
- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Installation Instructions](#installation-instructions)
- [Model Training](#model-training)
- [Model Deployment](#model-deployment)
- [Usage](#usage)
- [License](#license)

---

## **Project Overview**

The goal of this project is to build a machine learning model that can predict the **recurrence of thyroid cancer** based on various patient features, such as:
- **Age**
- **Gender**
- **Smoking history**
- **Treatment response**
- **Tumor stage** and more.

We used **Random Forest Classifier** for model training and **Recursive Feature Elimination (RFE)** for feature selection. The model is optimized using **RandomizedSearchCV** for hyperparameter tuning, and deployed via **Streamlit** to allow users to input patient data and get predictions.

---

## **Technologies Used**
- **Python**: Programming language used.
- **Pandas**: Data manipulation and analysis.
- **Scikit-learn**: Machine learning library (Random Forest, RFE, LabelEncoder, etc.).
- **Joblib**: For saving and loading models.
- **Streamlit**: Web app framework for deployment.
- **Matplotlib/Seaborn**: Data visualization.

---

## **Installation Instructions**

To get started, you need Python 3.x and the following libraries:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/thyroid-cancer-recurrence-prediction.git
   cd thyroid-cancer-recurrence-prediction
