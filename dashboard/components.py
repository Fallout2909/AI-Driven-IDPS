import streamlit as st


# ==========================================================
# PAGE TITLE
# ==========================================================

def page_title(title, subtitle=""):

    st.markdown(f"""
    <div style="
        padding:20px;
        border-radius:15px;
        background:linear-gradient(90deg,#1e3a8a,#2563eb);
        color:white;
        margin-bottom:25px;
    ">

    <h1 style="margin:0;">{title}</h1>

    <p style="margin:0;font-size:18px;">
        {subtitle}
    </p>

    </div>
    """, unsafe_allow_html=True)


# ==========================================================
# SECTION HEADER
# ==========================================================

def section(title):

    st.markdown(f"""
    <h2 style="
        color:#3b82f6;
        margin-top:25px;
        margin-bottom:15px;
    ">
    {title}
    </h2>
    """, unsafe_allow_html=True)


# ==========================================================
# STATUS CARD
# ==========================================================

def status_card(
    title,
    body,
    color="#2563eb"
):

    st.markdown(f"""
    <div style="
        background:#1e293b;
        border-left:6px solid {color};
        padding:20px;
        border-radius:15px;
        min-height:240px;
        margin-bottom:15px;
    ">

    <h3>{title}</h3>

    <hr>

    {body}

    </div>
    """, unsafe_allow_html=True)


# ==========================================================
# SUCCESS PANEL
# ==========================================================

def success_panel(message):

    st.success(message)


# ==========================================================
# WARNING PANEL
# ==========================================================

def warning_panel(message):

    st.warning(message)


# ==========================================================
# ERROR PANEL
# ==========================================================

def error_panel(message):

    st.error(message)


# ==========================================================
# INFORMATION PANEL
# ==========================================================

def info_panel(message):

    st.info(message)


# ==========================================================
# THREAT BADGE
# ==========================================================

def threat_badge(level):

    colours = {
        "LOW": "#22c55e",
        "MEDIUM": "#f59e0b",
        "HIGH": "#ef4444",
        "CRITICAL": "#991b1b"
    }

    colour = colours.get(level, "#2563eb")

    st.markdown(f"""
    <div style="
        display:inline-block;
        padding:10px 25px;
        border-radius:50px;
        background:{colour};
        color:white;
        font-size:18px;
        font-weight:bold;
    ">
    {level}
    </div>
    """, unsafe_allow_html=True)


# ==========================================================
# DETECTION PIPELINE
# ==========================================================

def detection_pipeline():

    st.markdown("""
```text
Network Traffic
        │
        ▼
 Data Preprocessing
        │
        ▼
 Isolation Forest
        │
        ▼
 Random Forest
        │
        ▼
 Threat Classification
        │
        ▼
 Alert Generation
        │
        ▼
 IP Blocking
        │
        ▼
 Dashboard Visualization
 
    """)