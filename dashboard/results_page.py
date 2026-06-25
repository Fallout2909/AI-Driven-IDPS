import streamlit as st
import pandas as pd

from components import page_title, section


def results_page():

    # ==========================================================
    # PAGE HEADER
    # ==========================================================

    page_title(
        "📊 Results & Evaluation",
        "Performance evaluation of the proposed AI-Driven Intrusion Detection and Prevention System."
    )

    st.divider()

    # ==========================================================
    # RANDOM FOREST
    # ==========================================================

    section("🌲 Random Forest Evaluation")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Accuracy", "99.73%")
    c2.metric("Precision", "0.87")
    c3.metric("Recall", "0.83")
    c4.metric("F1 Score", "0.84")

    st.write("")

    left, right = st.columns([3, 1.35])

    with left:

        st.image(
        "results/figures/random_forest_confusion_matrix.png",
        width=900
        )

    with right:

        st.markdown(
            """
<div style="background:#114d1e;
padding:20px;
border-radius:15px;
height:310px;">

<h2>🟢 Model Rating</h2>

**Performance Grade:** A+

**Accuracy:** 99.73%

**False Positives:** Very Low

**False Negatives:** Very Low

**Deployment Status:** Recommended

</div>
""",
            unsafe_allow_html=True,
        )

        st.write("")

        st.markdown(
            """
<div style="background:#163b63;
padding:20px;
border-radius:15px;
height:310px;">

<h2>📌 Key Findings</h2>

- Strong multi-class classification

- Excellent generalization

- Very low misclassification rate

- High attack detection capability

- Suitable for production deployment

</div>
""",
            unsafe_allow_html=True,
        )
        
        st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)

    st.success("""
### Interpretation

The Random Forest classifier achieved the highest performance among all evaluated models with an overall **accuracy of 99.73%**.

The confusion matrix demonstrates excellent classification capability across multiple attack categories while maintaining an extremely low false positive rate. These findings indicate that Random Forest is highly suitable as the primary intrusion classification engine.
""")

    st.divider()

    # ==========================================================
    # ISOLATION FOREST
    # ==========================================================

    section("🌳 Isolation Forest Evaluation")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Accuracy", "83.89%")
    c2.metric("Precision", "0.71")
    c3.metric("Recall", "0.69")
    c4.metric("F1 Score", "0.70")

    st.write("")

    left, right = st.columns([3, 1.48])

    with left:

        st.image(
            "results/figures/isolation_confusion_matrix.png",
            width=900
        )

    with right:

        st.markdown(
            """
<div style="background:#6b5f00;
padding:20px;
border-radius:15px;
height:300px;">

<h2>🟡 Model Rating</h2>

**Performance Grade:** B

**Accuracy:** 83.89%

**False Positives:** Moderate

**False Negatives:** Moderate

**Deployment Status:** Secondary Detection Layer

</div>
""",
            unsafe_allow_html=True,
        )

        st.write("")

        st.markdown(
            """
<div style="background:#163b63;
padding: 20px;
border-radius:15px;
height:300px;">

<h2>📌 Key Findings</h2>

- Effective anomaly detection

- Detects unknown attacks

- Unsupervised learning

- Useful secondary defense

- Complements Random Forest

</div>
""",
            unsafe_allow_html=True,
        )
        
        st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)

    st.info("""
### Interpretation

Isolation Forest achieved an overall **accuracy of 83.89%**.

Although its performance is lower than Random Forest, it provides valuable anomaly detection without requiring labelled attack data. Therefore, it serves as an effective first-stage screening model before supervised attack classification.
""")

    st.divider()

    # ==========================================================
    # MODEL COMPARISON
    # ==========================================================

    section("⚖️ Model Comparison")

    st.image(
        "results/figures/model_comparison.png",
        use_container_width=True
    )

    comparison = pd.DataFrame({

        "Model": [
            "Random Forest",
            "Isolation Forest"
        ],

        "Accuracy": [
            "99.73%",
            "83.89%"
        ],

        "Precision": [
            "0.87",
            "0.71"
        ],

        "Recall": [
            "0.83",
            "0.69"
        ],

        "F1 Score": [
            "0.84",
            "0.70"
        ]

    })

    st.dataframe(
        comparison,
        use_container_width=True,
        hide_index=True
    )

    st.success("""
## Recommended Hybrid Architecture

The experimental results demonstrate that **Random Forest** consistently outperformed Isolation Forest across all evaluation metrics.

The proposed AI-Driven IDPS therefore adopts a hybrid architecture:

• Isolation Forest performs anomaly detection.

• Random Forest performs attack classification.

• High-risk predictions trigger alert generation.

• The system simulates automatic IP blocking.

This layered design combines the strengths of supervised and unsupervised machine learning, improving overall detection capability and system robustness.
""")

    st.divider()

    # ==========================================================
    # FEATURE IMPORTANCE
    # ==========================================================

    section("🎯 Top 20 Important Features")

    st.image(
        "results/figures/feature_importance.png",
        use_container_width=True
    )

    st.info("""
### Feature Importance Analysis

The Random Forest feature importance analysis reveals that packet size and packet length related attributes contribute most significantly to intrusion detection performance.

The three most influential features are:

1. Average Backward Segment Size

2. Packet Length Standard Deviation

3. Packet Length Variance

These findings indicate that abnormal packet characteristics are strong indicators of malicious network activity within the CICIDS2017 dataset.
""")