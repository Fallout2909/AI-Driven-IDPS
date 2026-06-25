import os
import random
from datetime import datetime

import joblib
import numpy as np
import pandas as pd
import streamlit as st


# ==========================================================
# LOAD MODELS
# ==========================================================

@st.cache_resource
def load_models():

    rf = joblib.load("models/random_forest.pkl")

    iso = joblib.load("models/isolation_forest.pkl")

    feature_columns = joblib.load(
        "models/feature_columns.pkl"
    )

    return rf, iso, feature_columns


# ==========================================================
# LOAD DATASET
# ==========================================================

@st.cache_data
def load_dataset():

    df = pd.read_csv(
        "data/processed/sample_dataset.csv",
        low_memory=False
    )

    df.replace(
        [np.inf, -np.inf],
        np.nan,
        inplace=True
    )

    df.dropna(inplace=True)

    return df


# ==========================================================
# LOAD ALERTS
# ==========================================================

def load_alerts():

    logfile = "logs/alerts.csv"

    if os.path.exists(logfile):

        return pd.read_csv(logfile)

    return pd.DataFrame(
        columns=[
            "Timestamp",
            "Source_IP",
            "Destination_IP",
            "Protocol",
            "Actual_Label",
            "Predicted_Attack",
            "Risk_Level",
            "Blocked_IP",
        ]
    )


# ==========================================================
# SAVE ALERT
# ==========================================================

def save_alert(
    source_ip,
    destination_ip,
    protocol,
    actual_label,
    prediction,
    risk,
    blocked_ip,
):

    logfile = "logs/alerts.csv"

    new_alert = pd.DataFrame(
        [{
            "Timestamp": datetime.now(),
            "Source_IP": source_ip,
            "Destination_IP": destination_ip,
            "Protocol": protocol,
            "Actual_Label": actual_label,
            "Predicted_Attack": prediction,
            "Risk_Level": risk,
            "Blocked_IP": blocked_ip,
        }]
    )

    if os.path.exists(logfile):

        existing = pd.read_csv(logfile)

        updated = pd.concat(
            [existing, new_alert],
            ignore_index=True
        )

        updated.to_csv(
            logfile,
            index=False
        )

    else:

        new_alert.to_csv(
            logfile,
            index=False
        )


# ==========================================================
# RISK LEVEL
# ==========================================================

def calculate_risk(prediction):

    high = [
        "DDoS",
        "DoS Hulk",
        "PortScan",
        "Bot"
    ]

    medium = [
        "FTP-Patator",
        "SSH-Patator",
        "DoS GoldenEye"
    ]

    if prediction in high:

        return "HIGH"

    elif prediction in medium:

        return "MEDIUM"

    return "LOW"


# ==========================================================
# RANDOM IP
# ==========================================================

def random_ip():

    return (
        f"192.168."
        f"{random.randint(1,254)}."
        f"{random.randint(1,254)}"
    )


# ==========================================================
# CONFIDENCE
# ==========================================================

def prediction_confidence(model, X):

    try:

        confidence = (
            model.predict_proba(X).max() * 100
        )

        return round(confidence, 2)

    except:

        return 100.0