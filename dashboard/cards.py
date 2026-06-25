import streamlit as st


# ==========================================================
# METRIC CARD
# ==========================================================

def metric_card(title, value, color="#2563eb"):

    st.markdown(
        f"""
        <div style="
            background:#1e293b;
            border-left:6px solid {color};
            border-radius:15px;
            padding:20px;
            min-height:115px;
            box-shadow:0 3px 10px rgba(0,0,0,.25);
        ">

            <div style="
                color:#94a3b8;
                font-size:15px;
            ">
                {title}
            </div>

            <div style="
                font-size:40px;
                font-weight:bold;
                color:white;
                margin-top:10px;
            ">
                {value}
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


# ==========================================================
# INFORMATION CARD
# ==========================================================

def info_card(
    title,
    body,
    background,
    height=330
):

    st.markdown(
        f"""
        <div style="
            background:{background};
            border-radius:18px;
            padding:24px;
            min-height:{height}px;
            box-shadow:0 5px 15px rgba(0,0,0,.25);
        ">

        <h2 style="margin-bottom:20px;">
        {title}
        </h2>

        {body}

        </div>
        """,
        unsafe_allow_html=True,
    )


# ==========================================================
# INTERPRETATION CARD
# ==========================================================

def interpretation_card(title, text):

    st.markdown(
        f"""
        <div style="
            background:#123524;
            border-left:6px solid #22c55e;
            border-radius:16px;
            padding:24px;
            margin-top:20px;
        ">

        <h2>
        💡 {title}
        </h2>

        <p style="
            font-size:17px;
            line-height:1.8;
        ">
        {text}
        </p>

        </div>
        """,
        unsafe_allow_html=True,
    )


# ==========================================================
# DEPLOYMENT CARD
# ==========================================================

def deployment_card():

    st.markdown(
        """
        <div style="
            background:#123524;
            border-radius:18px;
            padding:25px;
            box-shadow:0 5px 15px rgba(0,0,0,.25);
        ">

        <h2>🛡 Deployment Recommendation</h2>

        <hr>

        <h3>Primary Model</h3>

        ✔ Random Forest

        <br><br>

        <h3>Secondary Layer</h3>

        ✔ Isolation Forest

        <br><br>

        <h3>Reason</h3>

        <ul>

        <li>Highest Accuracy</li>

        <li>Low False Positive Rate</li>

        <li>Detects Unknown Attacks</li>

        <li>Fast Prediction Speed</li>

        </ul>

        </div>
        """,
        unsafe_allow_html=True,
    )