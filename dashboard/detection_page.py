import random
import time

import pandas as pd
import streamlit as st

from components import (
    page_title,
    section,
    threat_badge,
)

from utils import (
    calculate_risk,
    prediction_confidence,
    random_ip,
    save_alert,
)


def detection_page(dataset, rf, iso, feature_columns):

    page_title(
        "🛡️ Detection Engine",
        "AI-powered Network Traffic Analysis"
    )

    # =====================================================
    # TRAFFIC SIMULATOR
    # =====================================================

    section("🌐 Network Traffic Simulator")

    col1, col2 = st.columns(2)

    with col1:

        source_ip = st.text_input(
            "Source IP",
            value=random_ip()
        )

        protocol = st.selectbox(
            "Protocol",
            [
                "TCP",
                "UDP",
                "ICMP"
            ]
        )

        source_port = st.number_input(
            "Source Port",
            1,
            65535,
            443
        )

    with col2:

        destination_ip = st.text_input(
            "Destination IP",
            value="10.0.0.15"
        )

        attack_type = st.selectbox(
            "Traffic Type",
            sorted(dataset[" Label"].unique())
        )

        destination_port = st.number_input(
            "Destination Port",
            1,
            65535,
            80
        )

    st.divider()

    # =====================================================
    # ANALYZE BUTTON
    # =====================================================

    if st.button(
        "🚀 Analyze Traffic",
        type="primary",
        use_container_width=True
    ):

        # -------------------------------------

        traffic = dataset[
            dataset[" Label"] == attack_type
        ]

        record = traffic.sample(1)

        actual_label = record[" Label"].values[0]

        X = record.drop(
            columns=[" Label"]
        )

        X = X[feature_columns]

        # -------------------------------------

        progress = st.progress(0)

        status = st.empty()

        steps = [

            "Capturing network packets...",

            "Extracting traffic features...",

            "Running Isolation Forest...",

            "Running Random Forest...",

            "Generating security decision..."
        ]

        for i, step in enumerate(steps):

            status.info(step)

            progress.progress(
                (i + 1) / len(steps)
            )

            time.sleep(0.6)

        status.empty()

        progress.empty()

        # =====================================================
        # MODELS
        # =====================================================

        iso_prediction = iso.predict(X)[0]

        anomaly = (
            "Suspicious"
            if iso_prediction == -1
            else "Normal"
        )

        prediction = rf.predict(X)[0]

        confidence = prediction_confidence(
            rf,
            X
        )

        risk = calculate_risk(
            prediction
        )

        # =====================================================
        # RESULTS
        # =====================================================

        section("📊 Detection Results")

        col1, col2, col3, col4, col5 = st.columns(5)

        col1.metric(
            "Actual",
            actual_label
        )

        col2.metric(
            "Predicted",
            prediction
        )

        col3.metric(
            "Confidence",
            f"{confidence:.2f}%"
        )

        col4.metric(
            "Anomaly",
            anomaly
        )

        col5.metric(
            "Protocol",
            protocol
        )

        st.divider()

        section("🚨 Threat Assessment")

        st.write("")

        if risk == "HIGH":

            st.error("""
### High Risk Threat Detected

Immediate action is recommended.

The detected traffic indicates a severe network attack that may impact availability or confidentiality.
""")

        elif risk == "MEDIUM":

            st.warning("""
### Medium Risk Threat

Suspicious activity detected.

Further monitoring is recommended.
""")

        else:

            st.success("""
### Low Risk

Traffic appears legitimate.

No immediate action required.
""")

        # =====================================================
        # RECOMMENDED ACTION
        # =====================================================

        section("🛡 Recommended Response")

        blocked_ip = ""

        if prediction != "BENIGN":

            blocked_ip = source_ip

            save_alert(
                source_ip,
                destination_ip,
                protocol,
                actual_label,
                prediction,
                risk,
                blocked_ip
            )

            st.success(f"""
### Incident Response Completed

- ✅ Alert Generated
- ✅ Event Logged
- ✅ Source IP Blocked

**Blocked IP Address**

`{blocked_ip}`
""")

        else:

            st.info("""
No blocking action required.

Traffic classified as BENIGN.
""")

        # =====================================================
        # TRAFFIC DETAILS
        # =====================================================

        section("📄 Traffic Information")

        info = pd.DataFrame({

            "Field":[
                "Source IP",
                "Destination IP",
                "Source Port",
                "Destination Port",
                "Protocol",
                "Traffic Type"
            ],

            "Value":[
                source_ip,
                destination_ip,
                source_port,
                destination_port,
                protocol,
                actual_label
            ]

        })

        st.dataframe(
            info,
            use_container_width=True,
            hide_index=True
        )