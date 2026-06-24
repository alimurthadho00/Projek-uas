import streamlit as st
import pandas as pd
import joblib
import os

# =========================
# LOAD MODEL
# =========================

BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, "best_model.pkl")

model = joblib.load(MODEL_PATH)

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Customer Retention Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# =========================
# HEADER
# =========================

st.title("📊 Customer Retention Analytics Dashboard")

st.markdown("""
Analisis perilaku pelanggan dan prediksi kemungkinan pelanggan
meninggalkan layanan menggunakan model Machine Learning Random Forest.
""")

# =========================
# SIDEBAR INPUT
# =========================

st.sidebar.header("📝 Customer Profile")

gender = st.sidebar.selectbox(
    "Gender",
    ["Male", "Female", "Other"]
)

age = st.sidebar.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=35
)

country = st.sidebar.selectbox(
    "Country",
    ["India", "Germany", "USA", "UK", "Bangladesh"]
)

city = st.sidebar.selectbox(
    "City",
    [
        "Berlin",
        "Mumbai",
        "London",
        "Hamburg",
        "New York",
        "Delhi",
        "Dhaka"
    ]
)

acquisition_channel = st.sidebar.selectbox(
    "Acquisition Channel",
    [
        "Email",
        "Organic",
        "Facebook Ads",
        "Referral",
        "Google Ads"
    ]
)

device_type = st.sidebar.selectbox(
    "Device Type",
    [
        "Tablet",
        "Desktop",
        "Mobile"
    ]
)

subscription_type = st.sidebar.selectbox(
    "Subscription Type",
    [
        "Annual",
        "Monthly"
    ]
)

is_premium_user = st.sidebar.selectbox(
    "Premium User",
    [0, 1]
)

total_visits = st.sidebar.number_input(
    "Total Visits",
    min_value=0,
    value=15
)

avg_session_time = st.sidebar.number_input(
    "Average Session Time",
    min_value=0.0,
    value=8.0
)

pages_per_session = st.sidebar.number_input(
    "Pages Per Session",
    min_value=0.0,
    value=4.0
)

email_open_rate = st.sidebar.slider(
    "Email Open Rate",
    0.0,
    1.0,
    0.5
)

email_click_rate = st.sidebar.slider(
    "Email Click Rate",
    0.0,
    1.0,
    0.2
)

total_spent = st.sidebar.number_input(
    "Total Spent",
    min_value=0.0,
    value=1000.0
)

avg_order_value = st.sidebar.number_input(
    "Average Order Value",
    min_value=0.0,
    value=50.0
)

discount_used = st.sidebar.selectbox(
    "Discount Used",
    [0, 1]
)

support_tickets = st.sidebar.number_input(
    "Support Tickets",
    min_value=0,
    value=2
)

refund_requested = st.sidebar.selectbox(
    "Refund Requested",
    [0, 1]
)

delivery_delay_days = st.sidebar.number_input(
    "Delivery Delay Days",
    min_value=0,
    value=2
)

payment_method = st.sidebar.selectbox(
    "Payment Method",
    [
        "UPI",
        "BKash",
        "PayPal",
        "SEPA",
        "Card"
    ]
)

satisfaction_score = st.sidebar.slider(
    "Satisfaction Score",
    1,
    5,
    4
)

nps_score = st.sidebar.slider(
    "NPS Score",
    0,
    10,
    7
)

marketing_spend_per_user = st.sidebar.number_input(
    "Marketing Spend Per User",
    min_value=0.0,
    value=15.0
)

lifetime_value = st.sidebar.number_input(
    "Lifetime Value",
    min_value=0.0,
    value=1200.0
)

last_3_month_purchase_freq = st.sidebar.number_input(
    "Last 3 Month Purchase Frequency",
    min_value=0,
    value=6
)

# =========================
# DASHBOARD CARDS
# =========================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Customer Age",
        age
    )

with col2:
    st.metric(
        "Lifetime Value",
        f"${lifetime_value:,.0f}"
    )

with col3:
    st.metric(
        "Total Visits",
        total_visits
    )

# =========================
# ENCODING
# =========================

gender_map = {
    "Female": 0,
    "Male": 1,
    "Other": 2
}

country_map = {
    "Bangladesh": 0,
    "Germany": 1,
    "India": 2,
    "UK": 3,
    "USA": 4
}

city_map = {
    "Berlin": 0,
    "Delhi": 1,
    "Dhaka": 2,
    "Hamburg": 3,
    "London": 4,
    "Mumbai": 5,
    "New York": 6
}

acquisition_map = {
    "Email": 0,
    "Facebook Ads": 1,
    "Google Ads": 2,
    "Organic": 3,
    "Referral": 4
}

device_map = {
    "Desktop": 0,
    "Mobile": 1,
    "Tablet": 2
}

subscription_map = {
    "Annual": 0,
    "Monthly": 1
}

payment_map = {
    "BKash": 0,
    "Card": 1,
    "PayPal": 2,
    "SEPA": 3,
    "UPI": 4
}

gender = gender_map[gender]
country = country_map[country]
city = city_map[city]
acquisition_channel = acquisition_map[acquisition_channel]
device_type = device_map[device_type]
subscription_type = subscription_map[subscription_type]
payment_method = payment_map[payment_method]

signup_date = 100
last_purchase_date = 200

# =========================
# PREDICTION
# =========================

if st.button("📊 Analyze Customer"):

    customer_profile = pd.DataFrame([[
        gender,
        age,
        country,
        city,
        signup_date,
        last_purchase_date,
        acquisition_channel,
        device_type,
        subscription_type,
        is_premium_user,
        total_visits,
        avg_session_time,
        pages_per_session,
        email_open_rate,
        email_click_rate,
        total_spent,
        avg_order_value,
        discount_used,
        support_tickets,
        refund_requested,
        delivery_delay_days,
        payment_method,
        satisfaction_score,
        nps_score,
        marketing_spend_per_user,
        lifetime_value,
        last_3_month_purchase_freq
    ]])

    retention_result = model.predict(customer_profile)

    st.subheader("Prediction Result")

    if retention_result[0] == 1:
        st.error("🚨 High Customer Churn Risk")
    else:
        st.success("🎉 Customer Likely To Stay")

    if hasattr(model, "predict_proba"):

        probability = model.predict_proba(
            customer_profile
        )

        churn_score = int(
            probability[0][1] * 100
        )

        st.subheader(
            "Customer Risk Analysis"
        )

        st.progress(churn_score)

        st.write(
            f"Churn Probability : {probability[0][1]*100:.2f}%"
        )

        st.write(
            f"Retention Probability : {probability[0][0]*100:.2f}%"
        )

        st.caption(
            f"Risk Score : {churn_score}%"
        )

# =========================
# FOOTER
# =========================

st.markdown("---")
st.caption(
    "Customer Retention Analytics Dashboard | Random Forest Model"
)