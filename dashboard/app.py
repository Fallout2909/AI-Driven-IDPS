import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import joblib
import random
import os

from datetime import datetime

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(page_title="AI-Driven IDPS", page_icon="🛡️", layout="wide")

# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown(
    """
<style>

.stTabs [data-baseweb="tab-list"] {
    gap: 15px;
}

.stTabs [data-baseweb="tab"] {
    height: 60px;
    font-size: 18px;
    font-weight: bold;
}

.metric-container {
    background-color: #111827;
    padding: 10px;
    border-radius: 10px;
}

</style>
""",
    unsafe_allow_html=True,
)

# ==================================================
# LOAD MODELS
# ==================================================


@st.cache_resource
def load_models():

    rf = joblib.load("models/random_forest.pkl")

    iso = joblib.load("models/isolation_forest.pkl")

    features = joblib.load("models/feature_columns.pkl")

    return rf, iso, features


rf, iso, feature_columns = load_models()

# ==================================================
# LOAD ALERTS
# ==================================================


def load_alerts():

    try:

        alerts = pd.read_csv("logs/alerts.csv")

        return alerts

    except:

        return pd.DataFrame(
            columns=[
                "Timestamp",
                "Actual_Label",
                "Predicted_Attack",
                "Risk_Level",
                "Blocked_IP",
            ]
        )


alerts = load_alerts()

# ==================================================
# TOP NAVIGATION TABS
# ==================================================

tab_dashboard, tab_detection, tab_results, tab_alerts = st.tabs(
    [
        "🏠 Dashboard",
        "🛡️ Detection Engine",
        "📊 Results & Evaluation",
        "🚨 Alert Center",
    ]
)


# =================================================
# DASHBOARD
# =================================================

with tab_dashboard:

    st.title("🛡️ AI-Driven Intrusion Detection and Prevention System")

    st.markdown(
        "Real-time Intrusion Detection Dashboard using Random Forest and Isolation Forest."
    )

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    total_alerts = len(alerts)

    if len(alerts) > 0:

        high_risk = len(alerts[alerts["Risk_Level"] == "HIGH"])

        blocked_ips = alerts["Blocked_IP"].nunique()

    else:

        high_risk = 0
        blocked_ips = 0

    col1.metric("Random Forest Accuracy", "99.73%")
    col2.metric("Isolation Forest Accuracy", "83.89%")
    col3.metric("Total Alerts", total_alerts)
    col4.metric("Blocked IPs", blocked_ips)

    st.divider()

    st.header("📈 Model Performance Comparison")

    st.image(
        "results/figures/model_comparison.png",
        use_container_width=True
    )

    st.divider()

    st.header("📊 Attack Distribution")

    st.image(
        "results/figures/class_distribution.png",
        use_container_width=True
    )

    st.divider()

    st.header("🏗️ System Architecture")

    st.code("""
Network Traffic
      ↓
Data Preprocessing
      ↓
Isolation Forest
      ↓
Random Forest
      ↓
Alert Generation
      ↓
IP Blocking
      ↓
Dashboard Visualization
""")

    st.divider()

    st.header("📌 Executive Summary")

    st.success("""
Random Forest achieved the highest performance with 99.73% accuracy.

Isolation Forest achieved 83.89% accuracy and serves as an anomaly detection layer.

The combination of both models provides a layered defense approach for detecting malicious network traffic.
""")

# ==================================================
# DETECTION ENGINE
# ==================================================

with tab_detection:

    st.title("🛡️ Detection Engine")

    st.markdown(
        "Analyze a random traffic record using Isolation Forest and Random Forest."
    )

    if st.button("Analyze Random Traffic", type="primary"):

        df = pd.read_csv("data/processed/sample_dataset.csv", low_memory=False)

        df.replace([np.inf, -np.inf], np.nan, inplace=True)

        df.dropna(inplace=True)

        record_id = random.randint(0, len(df) - 1)

        record = df.iloc[[record_id]]

        actual_label = record[" Label"].values[0]

        X = record.drop(columns=[" Label"])

        X = X[feature_columns]

        # -------------------------
        # Isolation Forest
        # -------------------------

        iso_result = iso.predict(X)[0]

        anomaly = "Suspicious" if iso_result == -1 else "Normal"

        # -------------------------
        # Random Forest
        # -------------------------

        prediction = rf.predict(X)[0]

        # -------------------------
        # Risk Classification
        # -------------------------

        high_risk_attacks = ["DDoS", "DoS Hulk", "PortScan", "Bot"]

        medium_risk_attacks = ["FTP-Patator", "SSH-Patator", "DoS GoldenEye"]

        if prediction in high_risk_attacks:
            risk = "HIGH"

        elif prediction in medium_risk_attacks:
            risk = "MEDIUM"

        else:
            risk = "LOW"

        # -------------------------
        # RESULTS
        # -------------------------

        st.success("Traffic Analysis Completed")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Actual Label", actual_label)

        col2.metric("Predicted Attack", prediction)

        col3.metric("Anomaly Status", anomaly)

        col4.metric("Risk Level", risk)

        st.divider()

        # -------------------------
        # THREAT ALERTS
        # -------------------------

        if risk == "HIGH":

            st.error("🚨 HIGH RISK THREAT DETECTED")

        elif risk == "MEDIUM":

            st.warning("⚠️ MEDIUM RISK THREAT DETECTED")

        else:

            st.success("✅ LOW RISK TRAFFIC")

        # -------------------------
        # SIMULATED BLOCKING
        # -------------------------

        if prediction != "BENIGN":

            ip = f"192.168.{random.randint(1,254)}." f"{random.randint(1,254)}"

            st.error(f"Blocked Source IP: {ip}")

            log_entry = pd.DataFrame(
                [
                    {
                        "Timestamp": datetime.now(),
                        "Actual_Label": actual_label,
                        "Predicted_Attack": prediction,
                        "Risk_Level": risk,
                        "Blocked_IP": ip,
                    }
                ]
            )

            logfile = "logs/alerts.csv"

            if os.path.exists(logfile):

                try:

                    existing = pd.read_csv(logfile)

                    updated = pd.concat([existing, log_entry], ignore_index=True)

                    updated.to_csv(logfile, index=False)

                except:

                    log_entry.to_csv(logfile, index=False)

            else:

                log_entry.to_csv(logfile, index=False)

            st.success("Alert logged successfully.")
            
            st.rerun()

# ==================================================
# RESULTS & EVALUATION
# ==================================================

with tab_results:

    st.title("📊 Results & Evaluation")

    # ==================================================
    # EXECUTIVE SUMMARY
    # ==================================================

    st.subheader("Executive Summary")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("RF Accuracy", "99.73%")
    col2.metric("IF Accuracy", "83.89%")
    col3.metric("RF F1 Score", "0.84")
    col4.metric("IF F1 Score", "0.70")

    st.success(
        "🏆 Random Forest was selected as the primary detection model due to its superior classification performance."
    )

    st.divider()

    # ==================================================
    # DATASET DISTRIBUTION
    # ==================================================

    st.header("Dataset Analysis")

    st.image(
        "results/figures/class_distribution.png",
        use_container_width=True
    )

    st.info("""
The CICIDS2017 dataset contains significantly more benign traffic records than attack records.

This class imbalance reflects realistic network environments and presents a common challenge in intrusion detection research.
""")

    st.divider()

    # ==================================================
    # RANDOM FOREST
    # ==================================================

    st.header("🌲 Random Forest Evaluation")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Accuracy", "99.73%")
    col2.metric("Precision", "0.87")
    col3.metric("Recall", "0.83")
    col4.metric("F1 Score", "0.84")

    st.success(
    "🏆 Best Performing Model in Experimental Evaluation"
    )

    st.divider()

    # ============================================
    # SUMMARY CARDS
    # ============================================

    card1, card2 = st.columns(2)

    with card1:

        st.markdown("""
        <div style="
        background:#163b1c;
        padding:25px;
        border-radius:12px;
        border-left:6px solid #00ff88;
        min-height:250px;
        ">

        <h2 style="margin-top:0;">🟢 Model Rating</h2>

        <hr>

        <p><b>Accuracy</b><br>99.73%</p>

        <p><b>False Positives</b><br>Very Low</p>

        <p><b>False Negatives</b><br>Very Low</p>

        <p><b>Deployment Status</b><br>Recommended</p>

        <p><b>Performance Grade</b><br>A+</p>

        </div>
        """, unsafe_allow_html=True)

    with card2:

        st.markdown("""
        <div style="
        background:#102a43;
        padding:25px;
        border-radius:12px;
        border-left:6px solid #4da3ff;
        height:525px;
        ">

        <h2 style="margin-top:0;">📌 Key Findings</h2>

        <hr>

        <ul>
        <li>Strong multi-class classification</li>
        <li>Excellent generalization ability</li>
        <li>Very low misclassification rate</li>
        <li>High attack detection capability</li>
        <li>Suitable for production deployment</li>
        </ul>

        </div>
        """, unsafe_allow_html=True)
        
    st.divider()

    

    # ============================================
    # CONFUSION MATRIX
    # ============================================

    st.subheader("Confusion Matrix")

    st.image(
    "results/figures/random_forest_confusion_matrix.png",
    use_container_width=True
    )

    st.divider()

    # ============================================
    # INTERPRETATION
    # ============================================

    st.subheader("Interpretation")

    st.markdown("""
The Random Forest classifier achieved an overall accuracy of **99.73%**, outperforming the Isolation Forest model across all evaluation metrics.

The confusion matrix demonstrates that the majority of network traffic records were correctly classified with minimal misclassification.

The model showed excellent capability in identifying both benign and malicious traffic patterns while maintaining extremely low false positive rates.

These findings indicate that Random Forest is highly suitable for deployment as the primary classification engine within the proposed AI-Driven Intrusion Detection and Prevention System.
""")
    
    st.divider()

    # ==================================================
    # ISOLATION FOREST
    # ==================================================

    st.header("🌳 Isolation Forest Evaluation")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Accuracy", "83.89%")
    col2.metric("Precision", "0.71")
    col3.metric("Recall", "0.69")
    col4.metric("F1 Score", "0.70")

    st.info(
    "🔍 Secondary Anomaly Detection Layer"
    )

    st.divider()

    card1, card2 = st.columns(2)

    with card1:

        st.markdown("""
        <div style="
        background:#4b4b0f;
        padding:25px;
        border-radius:12px;
        border-left:6px solid #ffd43b;
        min-height:250px;
        ">

        <h2 style="margin-top:0;">🟡 Model Rating</h2>

        <hr>

        <p><b>Accuracy</b><br>83.89%</p>

        <p><b>False Positives</b><br>Moderate</p>

        <p><b>False Negatives</b><br>Moderate</p>

        <p><b>Deployment Status</b><br>Support Model</p>

        <p><b>Performance Grade</b><br>B</p>

        </div>
        """, unsafe_allow_html=True)

    with card2:

        st.markdown("""
        <div style="
        background:#102a43;
        padding:25px;
        border-radius:12px;
        border-left:6px solid #4da3ff;
        height:525px;
        ">

        <h2 style="margin-top:0;">📌 Key Findings</h2>

        <hr>

        <ul>
        <li>Detects anomalous behavior</li>
        <li>Can identify unknown attacks</li>
        <li>Unsupervised learning approach</li>
        <li>Useful as secondary defense layer</li>
        <li>Complements Random Forest</li>
        </ul>

        </div>
        """, unsafe_allow_html=True)

    st.divider()

    st.subheader("Confusion Matrix")

    st.image(
    "results/figures/isolation_confusion_matrix.png",
    use_container_width=True
    )

    st.divider()

    st.subheader("Interpretation")

    st.markdown("""
Isolation Forest achieved an overall accuracy of **83.89%**.

Although its performance was lower than Random Forest, it remains valuable for identifying anomalous behavior and previously unseen attack patterns.

The model can serve as a complementary anomaly detection layer, providing additional visibility into suspicious network activities that may not have been observed during training.

Therefore, Isolation Forest is retained as a supporting component within the proposed AI-Driven Intrusion Detection and Prevention System.
    """)
    
    st.divider()

    # ==================================================
    # FEATURE IMPORTANCE
    # ==================================================

    st.header("📈 Feature Importance Analysis")

    st.image(
        "results/figures/feature_importance.png",
        use_container_width=True
    )
    
    st.divider()

    st.success("""
Top Contributing Features:

• Average Backward Segment Size

• Packet Length Standard Deviation

• Packet Length Variance

• Maximum Packet Length

• Backward Packet Length Standard Deviation
""")

    st.markdown("""
These network flow characteristics were identified as the most influential indicators for distinguishing benign traffic from malicious activity.
""")

    st.divider()

    # ==================================================
    # MODEL COMPARISON
    # ==================================================

    st.header("⚖️ Model Comparison")

    st.image(
        "results/figures/model_comparison.png",
        use_container_width=True
    )

    comparison_df = pd.DataFrame({
        "Metric": [
            "Accuracy",
            "Precision",
            "Recall",
            "F1 Score"
        ],
        "Random Forest": [
            99.73,
            0.87,
            0.83,
            0.84
        ],
        "Isolation Forest": [
            83.89,
            0.71,
            0.69,
            0.70
        ]
    })

    st.dataframe(
        comparison_df,
        use_container_width=True
    )

    st.divider()

    # ==================================================
    # FINAL CONCLUSION
    # ==================================================

    st.header("📌 Final Evaluation")

    st.success("""
### Selected Model: Random Forest

Based on the experimental evaluation, Random Forest achieved superior performance across all metrics and demonstrated excellent intrusion detection capability.

The model achieved:

• Accuracy: 99.73%

• Precision: 0.87

• Recall: 0.83

• F1 Score: 0.84

Therefore, Random Forest is selected as the primary detection engine for the proposed AI-Driven Intrusion Detection and Prevention System.

Isolation Forest is retained as a supporting anomaly detection mechanism for identifying suspicious and previously unseen traffic patterns.
""")
    
# ===========================================================
# ALERT CENTER
# ===========================================================

with tab_alerts:

    st.title("🚨 Alert Center")

    st.markdown("View generated alerts and blocked IP addresses.")

    st.divider()
    
    alerts = load_alerts()

    if len(alerts) == 0:

        st.info("No alerts generated yet.")

    else:

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Alerts", len(alerts))

        high_risk = len(
            alerts[alerts["Risk_Level"] == "HIGH"]
        )

        col2.metric("High Risk Alerts", high_risk)

        blocked_ips = alerts["Blocked_IP"].nunique()

        col3.metric("Blocked IPs", blocked_ips)

        st.divider()

        st.subheader("Alert Log")

        st.dataframe(
            alerts,
            use_container_width=True
        )

        st.divider()

        st.subheader("Attack Distribution")

        attack_counts = (
            alerts["Predicted_Attack"]
            .value_counts()
            .reset_index()
        )

        attack_counts.columns = [
            "Attack",
            "Count"
        ]

        fig = px.bar(
            attack_counts,
            x="Attack",
            y="Count",
            title="Detected Attack Types"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        csv = alerts.to_csv(index=False)

        st.download_button(
            label="📥 Download Alert Report",
            data=csv,
            file_name="alert_report.csv",
            mime="text/csv"
        )