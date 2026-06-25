import streamlit as st

from styles import load_css

from utils import (
    load_models,
    load_dataset,
    load_alerts,
)

from dashboard_page import dashboard_page
from detection_page import detection_page
from results_page import results_page
from alerts_page import alerts_page


# ======================================================
# PAGE CONFIG
# ======================================================

st.set_page_config(
    page_title="AI-Driven IDPS",
    page_icon="🛡️",
    layout="wide"
)

load_css()


# ======================================================
# LOAD SHARED RESOURCES
# ======================================================

rf, iso, feature_columns = load_models()

dataset = load_dataset()

alerts = load_alerts()


# ======================================================
# HEADER
# ======================================================

st.markdown("""
<h1 style='margin-bottom:5px;'>
🛡️ AI-Driven Intrusion Detection and Prevention System
</h1>
""", unsafe_allow_html=True)

st.caption(
    "SEC3044 • AI-Based Network Intrusion Detection using Random Forest and Isolation Forest"
)


# ======================================================
# NAVIGATION
# ======================================================

tab_dashboard, tab_detection, tab_results, tab_alerts = st.tabs(
    [
        "🏠 Dashboard",
        "🛡️ Detection Engine",
        "📊 Results & Evaluation",
        "🚨 Alert Center"
    ]
)


# ======================================================
# DASHBOARD
# ======================================================

with tab_dashboard:

    dashboard_page(alerts)


# ======================================================
# DETECTION ENGINE
# ======================================================

with tab_detection:

    detection_page(
        dataset,
        rf,
        iso,
        feature_columns
    )


# ======================================================
# RESULTS
# ======================================================

with tab_results:

    results_page()


# ======================================================
# ALERTS
# ======================================================

with tab_alerts:

    alerts_page()