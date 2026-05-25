import streamlit as st
from recepcion import show_recepcion
from pagos import show_pagos
from dashboard import show_dashboard

# Configuración general
st.set_page_config(page_title="ClifermProject IA - App", layout="wide")

# --- NAVEGACIÓN ---
st.sidebar.title("🏢 ClifermProject IA")
st.sidebar.markdown("Sistema de Gestión Bancaria")
page = st.sidebar.radio("Ir a:", ["📥 Recepción y OCR", "💰 Gestión de Pagos", "📊 Dashboard Estratégico"])

if page == "📥 Recepción y OCR":
    show_recepcion()
elif page == "💰 Gestión de Pagos":
    show_pagos()
elif page == "📊 Dashboard Estratégico":
    show_dashboard()