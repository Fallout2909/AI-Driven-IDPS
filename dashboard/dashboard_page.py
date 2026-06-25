import pandas as pd
import plotly.express as px
import streamlit as st

from components import (
    page_title,
    section,
    detection_pipeline,
)


def dashboard_page(alerts):

    page_title(
        "🏠 Dashboard",
        "Real-time overview of the AI-Driven Intrusion Detection and Prevention System"
    )

    # ======================================================
    # KPI CARDS
    # ======================================================

    total_alerts = len(alerts)

    blocked_ips = (
        alerts["Blocked_IP"].nunique()
        if not alerts.empty and "Blocked_IP" in alerts.columns
        else 0
    )

    high_risk = (
        len(alerts[alerts["Risk_Level"] == "HIGH"])
        if not alerts.empty and "Risk_Level" in alerts.columns
        else 0
    )

    medium_risk = (
        len(alerts[alerts["Risk_Level"] == "MEDIUM"])
        if not alerts.empty and "Risk_Level" in alerts.columns
        else 0
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "🌲 Random Forest",
        "99.73%"
    )

    col2.metric(
        "🌳 Isolation Forest",
        "83.89%"
    )

    col3.metric(
        "🚨 Total Alerts",
        total_alerts
    )

    col4.metric(
        "🛑 Blocked IPs",
        blocked_ips
    )

    st.divider()

    # ======================================================
    # MODEL PERFORMANCE
    # ======================================================

    section("📈 Model Performance Comparison")

    st.image(
        "results/figures/model_comparison.png",
        use_container_width=True
    )

    st.divider()

    # ======================================================
    # ATTACK DISTRIBUTION
    # ======================================================

    section("📊 Threat Overview")

    left, right = st.columns([2, 1])

    with left:

        st.image(
            "results/figures/class_distribution.png",
            use_container_width=True
        )

    with right:

        if total_alerts > 0:

            risk_df = pd.DataFrame({
                "Risk": [
                    "High",
                    "Medium"
                ],
                "Count": [
                    high_risk,
                    medium_risk
                ]
            })

            fig = px.pie(
                risk_df,
                values="Count",
                names="Risk",
                hole=0.45
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        else:

            st.info(
                "No alerts have been generated yet."
            )

    st.divider()

    # ======================================================
    # RECENT ALERTS
    # ======================================================

    section("🚨 Recent Security Events")

    if alerts.empty:

        st.info(
            "No security events recorded."
        )

    else:

        st.dataframe(
            alerts.tail(10),
            use_container_width=True,
            hide_index=True
        )

    st.divider()

    # ======================================================
    # SYSTEM ARCHITECTURE
    # ======================================================

    section("🏗 System Workflow")

    detection_pipeline()

    st.divider()

    # ======================================================
    # EXECUTIVE SUMMARY
    # ======================================================

    section("📌 Executive Summary")

    st.success("""
### AI-Driven Intrusion Detection and Prevention System

The proposed system combines **Isolation Forest** and **Random Forest** to provide a layered intrusion detection approach.

#### Key Highlights

- ✅ Random Forest achieved **99.73% accuracy**
- ✅ Isolation Forest provides anomaly detection capabilities
- ✅ Automatic alert generation
- ✅ Simulated IP blocking
- ✅ Interactive Streamlit dashboard
- ✅ Real-time attack analysis
- ✅ SOC-style monitoring interface
""")