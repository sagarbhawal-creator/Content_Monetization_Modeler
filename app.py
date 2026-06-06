import streamlit as st
import pandas as pd
import joblib
from datetime import date

# Page Configuration
st.title("📺 YouTube Ad Revenue Predictor")

st.write(
    "Predict estimated YouTube ad revenue based on video performance metrics."
)

# Load Saved Files
model = joblib.load("youtube_revenue_model.pkl")

scaler = joblib.load("scaler.pkl")

feature_columns = joblib.load("feature_columns.pkl")

# Create User Inputs
views = st.number_input(
    "Views",
    min_value=0,
    value=1000
)

likes = st.number_input(
    "Likes",
    min_value=0,
    value=100
)

comments = st.number_input(
    "Comments",
    min_value=0,
    value=20
)

watch_time_minutes = st.number_input(
    "Watch Time (Minutes)",
    min_value=0.0,
    value=1000.0
)

video_length_minutes = st.number_input(
    "Video Length (Minutes)",
    min_value=0.0,
    value=10.0
)

subscribers = st.number_input(
    "Subscribers",
    min_value=0,
    value=5000
)

# Date Input
selected_date = st.date_input(
    "Upload Date",
    value=date.today()
)

year = selected_date.year
month = selected_date.month
day = selected_date.day
day_of_week = selected_date.weekday()

# Category Dropdown
category = st.selectbox(
    "Category",
    [
        "Education",
        "Entertainment",
        "Gaming",
        "Lifestyle",
        "Music",
        "Tech"
    ]
)

# Device Dropdown
device = st.selectbox(
    "Device",
    [
        "Desktop",
        "Mobile",
        "TV",
        "Tablet"
    ]
)

# Country Dropdown
country = st.selectbox(
    "Country",
    [
        "AU",
        "CA",
        "DE",
        "IN",
        "UK",
        "US"
    ]
)

# Creating Predict Button
if st.button("Predict Revenue"):

    input_dict = {
        'views': views,
        'likes': likes,
        'comments': comments,
        'watch_time_minutes': watch_time_minutes,
        'video_length_minutes': video_length_minutes,
        'subscribers': subscribers,
        'year': year,
        'month': month,
        'day': day,
        'day_of_week': day_of_week
    }

    # Category Encoding
    input_dict['category_Entertainment'] = 1 if category == 'Entertainment' else 0
    input_dict['category_Gaming'] = 1 if category == 'Gaming' else 0
    input_dict['category_Lifestyle'] = 1 if category == 'Lifestyle' else 0
    input_dict['category_Music'] = 1 if category == 'Music' else 0
    input_dict['category_Tech'] = 1 if category == 'Tech' else 0

    # Device Encoding
    input_dict['device_Mobile'] = 1 if device == 'Mobile' else 0
    input_dict['device_TV'] = 1 if device == 'TV' else 0
    input_dict['device_Tablet'] = 1 if device == 'Tablet' else 0

    # Country Encoding
    input_dict['country_CA'] = 1 if country == 'CA' else 0
    input_dict['country_DE'] = 1 if country == 'DE' else 0
    input_dict['country_IN'] = 1 if country == 'IN' else 0
    input_dict['country_UK'] = 1 if country == 'UK' else 0
    input_dict['country_US'] = 1 if country == 'US' else 0

    # Convert to DataFrame
    input_df = pd.DataFrame([input_dict])

    # Match Training Columns
    input_df = input_df.reindex(
        columns=feature_columns,
        fill_value=0
    )

    # Scale Input
    input_scaled = scaler.transform(input_df)

    # Predict Revenue
    prediction = model.predict(input_scaled)

    # Display Result
    st.success(
        f"Estimated Ad Revenue: ${prediction[0]:.2f}"
    )

# About model usage and predictions
st.sidebar.header("Project Information")

st.sidebar.write("""
Model: Linear Regression

R² Score: 0.9526

MAE: 3.11

RMSE: 13.48
""")

