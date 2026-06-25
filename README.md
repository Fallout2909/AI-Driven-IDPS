# 🛡️ AI-Driven Intrusion Detection and Prevention System (AI-Driven IDPS)

An AI-powered Intrusion Detection and Prevention System (IDPS) developed for **SEC3044 – Advanced Topics in Computer Security** at **Sunway University**.

The project combines **Machine Learning**, **Anomaly Detection**, and an **interactive Streamlit dashboard** to identify malicious network traffic, generate security alerts, and simulate automated prevention mechanisms.

---

# 📌 Project Overview

Traditional Intrusion Detection Systems often rely on signature-based detection and are unable to identify new or previously unseen attacks.

This project implements an intelligent AI-driven IDPS that combines:

- 🌲 Random Forest (Supervised Attack Classification)
- 🌳 Isolation Forest (Unsupervised Anomaly Detection)

The system analyses network traffic from the CICIDS2017 dataset and performs:

- Attack Classification
- Anomaly Detection
- Threat Assessment
- Alert Generation
- Simulated IP Blocking
- Interactive Security Dashboard

---

# 🚀 Features

## Machine Learning

- Random Forest multi-class classifier
- Isolation Forest anomaly detector
- Confidence score prediction
- Risk level calculation

---

## Intrusion Detection

- Detects multiple network attacks
- Identifies anomalous traffic
- Distinguishes BENIGN traffic from attacks
- Generates real-time threat assessment

---

## Intrusion Prevention

- Automatic alert generation
- Simulated IP blocking
- Alert logging
- Security event recording

---

## Interactive Dashboard

Built using **Streamlit**.

Features include:

- 📊 Dashboard Overview
- 🛡️ Detection Engine
- 📈 Results & Evaluation
- 🚨 Alert Center

---

# 🖥️ Dashboard Preview

### Dashboard

Displays:

- Model Accuracy
- Alert Statistics
- Detection Summary
- System Overview

---

### Detection Engine

Allows users to simulate network traffic by selecting:

- Source IP
- Destination IP
- Protocol
- Traffic Type

The system performs:

- Isolation Forest anomaly detection
- Random Forest attack classification
- Confidence estimation
- Threat assessment
- Simulated IP blocking

---

### Results & Evaluation

Visualises:

- Random Forest Confusion Matrix
- Isolation Forest Confusion Matrix
- Feature Importance
- Model Comparison
- Classification Metrics
- Deployment Recommendation

---

### Alert Center

Displays:

- Generated Alerts
- Threat Log
- Blocked IP Addresses
- Alert History

---

# 📂 Project Structure

```
AI-DRIVEN-IDPS
│
├── dashboard/
│   ├── app.py
│   ├── dashboard_page.py
│   ├── detection_page.py
│   ├── results_page.py
│   ├── alerts_page.py
│   ├── cards.py
│   ├── components.py
│   ├── styles.py
│   └── utils.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── logs/
│   └── alerts.csv
│
├── models/
│   ├── random_forest.pkl
│   ├── isolation_forest.pkl
│   └── feature_columns.pkl
│
├── results/
│   ├── figures/
│   └── metrics/
│
├── src/
│   ├── data/
│   └── models/
│
├── requirements.txt
└── README.md
```

---

# 📊 Dataset

Dataset used:

**CICIDS2017**

Download:

https://www.kaggle.com/datasets/chethuhn/network-intrusion-dataset

The dataset contains both normal and malicious network traffic, including:

- BENIGN
- DDoS
- DoS Hulk
- DoS GoldenEye
- PortScan
- Bot
- FTP-Patator
- SSH-Patator
- Brute Force
- XSS
- Slowloris
- Slow HTTP Test

---

# 🤖 Machine Learning Models

## Random Forest

Purpose:

Supervised multi-class attack classification.

Performance:

- Accuracy: **99.73%**

Advantages:

- Excellent classification accuracy
- Low false positive rate
- Suitable for deployment

---

## Isolation Forest

Purpose:

Unsupervised anomaly detection.

Performance:

- Accuracy: **83.89%**

Advantages:

- Detects unknown attacks
- Complements Random Forest
- Useful as a secondary defence layer

---

# 📈 Experimental Results

| Model | Accuracy |
|---------|----------|
| Random Forest | **99.73%** |
| Isolation Forest | **83.89%** |

Random Forest achieved the highest performance and is recommended as the primary classification model.

---

# 🛠️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/AI-Driven-IDPS.git
```

Move into the project

```bash
cd AI-Driven-IDPS
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Dashboard

Launch Streamlit

```bash
streamlit run dashboard/app.py
```

The dashboard will open automatically in your browser.

---

# 📝 Future Improvements

Possible future enhancements include:

- Real-time packet capture using Scapy or PyShark
- Integration with Suricata or Snort
- Deep Learning models (LSTM, CNN, Transformer)
- Live network monitoring
- Firewall API integration
- Threat Intelligence feeds
- Explainable AI (SHAP)
