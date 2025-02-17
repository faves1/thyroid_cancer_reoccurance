# **Thyroid Cancer Recurrence Prediction Model**

This project uses machine learning to predict the likelihood of recurrence in thyroid cancer patients based on various clinical and demographic factors. The model is built using **Random Forest** and optimized with **hyperparameter tuning** and **feature selection**. The model is deployed using **Streamlit** for easy access and user interaction.
**Live Link** : https://thyroid-reoccurance-prediction.streamlit.app/

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

## **Model Training**
To train the model, we used a dataset with the following features:

- **Demographics**: Age, gender, smoking history.
- **Clinical features**: Tumor size, lymph node involvement, cancer stage, and treatment response.
1. **Data Preprocessing:**

    - Handling missing values, duplicates.
    - Encoding categorical variables using LabelEncoder.
    - Scaling numerical features (like Age) using StandardScaler.
    
2. **Model Building:**

  - We built a Random Forest Classifier model and optimized it using RandomizedSearchCV for hyperparameter tuning.
  - Recursive Feature Elimination (RFE) was used to select the top 7 most important features.

3. **Model Saving:**

The trained model is saved using joblib (thyroid_recurrence_model.pkl).
