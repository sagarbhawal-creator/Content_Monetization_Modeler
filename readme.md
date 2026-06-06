# 📺 Content Monetization Modeler

## Project Overview

The Content Monetization Modeler is a Machine Learning project that predicts YouTube ad revenue based on video performance metrics such as views, likes, comments, watch time, subscribers, category, device type, and country.

The project includes data preprocessing, exploratory data analysis (EDA), feature engineering, model training, model evaluation, and deployment using Streamlit.

---

## Problem Statement

Content creators and businesses often want to estimate the revenue potential of their videos before publishing or during performance tracking.

This project aims to build a predictive model that estimates ad revenue using historical video performance data.

---

## Dataset Information

### Dataset Size

- Records: 122,400
- Features: 12

### Features

| Feature | Description |
|----------|------------|
| video_id | Unique video identifier |
| date | Upload/observation date |
| views | Number of views |
| likes | Number of likes |
| comments | Number of comments |
| watch_time_minutes | Total watch time |
| video_length_minutes | Video duration |
| subscribers | Subscriber count |
| category | Video category |
| device | Viewing device |
| country | Viewer country |
| ad_revenue_usd | Revenue generated (Target Variable) |

---

## Project Workflow

### 1. Data Cleaning

- Handled missing values using Mean Imputation
- Removed duplicate records
- Converted date column to datetime format
- Removed unnecessary identifier column (`video_id`)

---

### 2. Exploratory Data Analysis (EDA)

Performed:

- Revenue Distribution Analysis
- Revenue Boxplot Analysis
- Correlation Heatmap
- Category-wise Revenue Analysis
- Device-wise Revenue Analysis
- Country-wise Revenue Analysis

### Key Findings

- Watch Time showed the strongest relationship with revenue.
- Likes contributed positively to revenue.
- Views alone had limited predictive power.
- Device and Country had relatively small influence.
- Revenue distribution was approximately normal.

---

### 3. Feature Engineering

Extracted new date features:

- Year
- Month
- Day
- Day of Week

Applied One-Hot Encoding on:

- Category
- Device
- Country

---

### 4. Feature Scaling

Used:

```python
StandardScaler()
```

to normalize numerical features before training Linear Regression, Ridge Regression, and Lasso Regression models.

---

## Machine Learning Models

The following regression models were trained and evaluated:

1. Linear Regression
2. Ridge Regression
3. Lasso Regression
4. Decision Tree Regressor
5. Random Forest Regressor

---

## Model Performance

| Model | R² Score | MAE | RMSE |
|---------|---------:|---------:|---------:|
| Linear Regression | 0.95258 | 3.114 | 13.479 |
| Ridge Regression | 0.95258 | 3.114 | 13.479 |
| Lasso Regression | 0.95258 | 3.138 | 13.479 |
| Decision Tree Regressor | 0.94967 | 4.643 | 13.887 |
| Random Forest Regressor | 0.95067 | 3.642 | 13.748 |

---

## Best Model

### Linear Regression

Selected as the final model because:

- Highest R² Score
- Lowest prediction error
- Fast training time
- Easy interpretation
- Simpler deployment

### Final Performance

- R² Score: 0.9526
- MAE: 3.11
- RMSE: 13.48

---

## Streamlit Application

A Streamlit web application was developed to allow users to:

- Enter video metrics
- Select category, device, and country
- Choose upload date
- Predict estimated ad revenue instantly

### Features

- Interactive User Interface
- Real-Time Prediction
- Trained Model Integration
- Automatic Feature Engineering
- Data Scaling Before Prediction

---

## Project Structure

```text
Content_Monetization_Modeler/
│
├── app.py
├── Content_Monetization_Modeler.ipynb
├── youtube_revenue_model.pkl
├── scaler.pkl
├── feature_columns.pkl
├── requirements.txt
├── README.md
└── screenshots/
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Content_Monetization_Modeler.git
```

Navigate to project folder:

```bash
cd Content_Monetization_Modeler
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Streamlit App

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Joblib
- Streamlit
- Git
- GitHub

---

## Business Insights

- Watch Time is the strongest predictor of revenue.
- User engagement metrics improve revenue estimation.
- Revenue prediction can achieve approximately 95% accuracy.
- Device and geographical differences contribute less than engagement metrics.

---

## Future Enhancements

- Hyperparameter Tuning
- XGBoost Regression
- Feature Importance Dashboard
- Cloud Deployment
- Real YouTube Analytics Integration

---

## Conclusion

This project successfully developed a machine learning solution capable of predicting YouTube ad revenue with high accuracy. Among the evaluated models, Linear Regression provided the best balance between performance, simplicity, and interpretability, achieving an R² score of approximately 95%.

---