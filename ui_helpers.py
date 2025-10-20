import streamlit as st

# Centralized UI helpers: page config, custom CSS, and small components

def set_page_config():
    st.set_page_config(
        page_title="자동차 구매 금액 예측",
        page_icon="🚗",
        layout="wide",
        initial_sidebar_state="expanded",
    )


def inject_css():
    css = """
    <style>
    /* Light mode base */
    :root {
        --bg-start: #f7fbff;
        --bg-end: #ffffff;
        --card-bg: #ffffff;
        --text-primary: #0f172a;
        --text-secondary: #475569;
        --muted: #94a3b8;
        --accent-1: #06b6d4;
        --accent-2: #3b82f6;
        --shadow: 0 6px 18px rgba(17, 24, 39, 0.08);
    }

    .stApp { background: linear-gradient(180deg, var(--bg-start) 0%, var(--bg-end) 100%); color: var(--text-primary); }

    /* Sidebar tweaks */
    .sidebar .css-1d391kg, .css-1d391kg .css-1d391kg { padding-top: 1rem; }

    /* Card */
    .card {
        background: var(--card-bg);
        padding: 1.1rem 1.2rem;
        border-radius: 12px;
        box-shadow: var(--shadow);
        margin-bottom: 1rem;
    }

    .big-title {
        font-size: 28px !important;
        font-weight: 700 !important;
        color: var(--text-primary) !important;
    }

    .subtitle {
        color: var(--text-secondary) !important;
        font-size: 14px !important;
    }

    .metric-box {
        background: linear-gradient(90deg,#eef2ff,#ffffff);
        border-radius: 10px;
        padding: 12px;
        text-align: center;
    }

    /* Button styles */
    .stButton>button {
        background: linear-gradient(90deg,var(--accent-1),var(--accent-2)) !important;
        color: white !important;
        border-radius: 10px !important;
        border: none !important;
        padding: 8px 12px !important;
        box-shadow: 0 6px 12px rgba(59,130,246,0.18) !important;
        font-weight: 600 !important;
    }

    /* Dataframe/Table styles */
    .dataframe, table {
        border-radius: 8px;
        overflow: hidden;
    }

    /* Dark mode overrides */
    @media (prefers-color-scheme: dark) {
        :root {
            --bg-start: #0b1220;
            --bg-end: #071024;
            --card-bg: #071427;
            --text-primary: #e6eef8;
            --text-secondary: #94a3b8;
            --muted: #9aa6b2;
            --accent-1: #06b6d4;
            --accent-2: #60a5fa;
            --shadow: 0 6px 18px rgba(2,6,23,0.7);
        }

        .stApp { background: linear-gradient(180deg, var(--bg-start) 0%, var(--bg-end) 100%); color: var(--text-primary); }

        .card { background: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01)); border: 1px solid rgba(255,255,255,0.03); }

        .big-title { color: var(--text-primary) !important; }
        .subtitle { color: var(--text-secondary) !important; }

        .metric-box { background: linear-gradient(90deg, rgba(11,24,40,0.6), rgba(7,20,36,0.4)); }

        /* Make default Streamlit text and inputs more legible */
        .stText, .stMarkdown, .css-1d391kg, .stApp * { color: var(--text-primary) !important; }
        .stButton>button { box-shadow: 0 6px 12px rgba(96,165,250,0.08) !important; }
    }

    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


def two_columns(widths=(6,4)):
    return st.columns(widths)


def info_card(title, text):
    st.markdown(f"<div class='card'><div class='big-title'>{title}</div><div class='subtitle'>{text}</div></div>", unsafe_allow_html=True)
