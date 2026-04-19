import streamlit as st
import streamlit.components.v1 as components
import os

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="BANGLADESH RUNNER",
    page_icon="🏃",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Hide all Streamlit chrome ─────────────────────────────────────────────────
st.markdown("""
<style>
  #MainMenu, header, footer, .stDeployButton,
  [data-testid="stToolbar"], [data-testid="stDecoration"],
  [data-testid="stStatusWidget"] { display: none !important; }

  html, body, [data-testid="stAppViewContainer"],
  [data-testid="stMain"], .main, .block-container {
    margin: 0 !important;
    padding: 0 !important;
    overflow: hidden !important;
    background: #87CEEB !important;
    max-width: 100% !important;
  }

  iframe {
    display: block;
    border: none;
    width: 100vw !important;
    height: 100vh !important;
  }
</style>
""", unsafe_allow_html=True)

# ── Load game HTML ────────────────────────────────────────────────────────────
game_file = os.path.join(os.path.dirname(__file__), "game.html")

if not os.path.exists(game_file):
    st.error("⚠️  game.html not found. Make sure it's in the same folder as app.py.")
    st.stop()

with open(game_file, "r", encoding="utf-8") as f:
    game_html = f.read()

# ── Render full viewport ──────────────────────────────────────────────────────
components.html(game_html, height=950, scrolling=False)
