import streamlit as st


def load_css():

    st.markdown(
        """
    <style>

    /* Hide Streamlit branding */
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    /* Main App */
    .stApp{
        background:#0f172a;
        color:white;
    }

    /* Tabs */

    .stTabs{

    margin-top:10px;
    margin-bottom:20px;

    }

    .stTabs [data-baseweb="tab-list"]{

    justify-content:center;

    gap:8px;

    border-bottom:none !important;

    }

    .stTabs [data-baseweb="tab-highlight"]{

    display:none;

    }

    .stTabs [data-baseweb="tab"]{

    min-width:165px;

    height:46px;

    border-radius:12px;

    background:#1e293b;

    color:white;

    font-size:16px;

    font-weight:600;

    border:none;

    transition:0.25s;

    }

    .stTabs [data-baseweb="tab"]:hover{

    background:#334155;

    }

    .stTabs [aria-selected="true"]{

    background:linear-gradient(
        90deg,
        #2563eb,
        #3b82f6
    );

    color:white;

    }
    
    /* Remove grey divider */

    .stTabs [data-baseweb="tab-border"]{

    display:none !important;

    }

    /* Metric Cards */

    div[data-testid="metric-container"]{

        background:#1e293b;

        border-radius:15px;

        padding:20px;

        border:1px solid #334155;

        box-shadow:0 4px 15px rgba(0,0,0,0.25);

    }

    div[data-testid="metric-container"]:hover{

        transform:translateY(-3px);

        transition:0.2s;

        border:1px solid #3b82f6;

    }

    /* Buttons */

    .stButton>button{

        width:100%;

        border-radius:12px;

        height:50px;

        font-size:18px;

        font-weight:bold;

        background:#2563eb;

        color:white;

    }

    .stButton>button:hover{

        background:#1d4ed8;

    }

    /* DataFrame */

    div[data-testid="stDataFrame"]{

        border-radius:15px;

        overflow:hidden;

    }

    h1{

        color:white;

    }

    h2{

        color:white;

    }

    h3{

        color:white;

    }

    hr{

        border:1px solid #334155;

    }

    </style>
    """,
        unsafe_allow_html=True,
    )
