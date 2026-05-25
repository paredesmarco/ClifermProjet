import streamlit as st
import pandas as pd
import plotly.express as px

def show_pagos():
    st.header("💰 Tesorería y Programación de Pagos")
    st.info("Perfil: Tesorero / Jefe de Finanzas")

    monto_disponible = st.slider("Definir Presupuesto de Pago Diario ($)", 0, 50000, 25000)
    
    st.subheader("Top Proveedores con Montos Pendientes")
    data_liq = pd.DataFrame({
        'Proveedor': ['Microsoft', 'Constructora Alfa', 'Energía Q.', 'Seguros Global'],
        'Monto ($)': [12500, 9800, 7500, 5200]
    })
    fig_liq = px.bar(data_liq, x='Monto ($)', y='Proveedor', orientation='h', color='Monto ($)')
    st.plotly_chart(fig_liq, use_container_width=True)

    st.subheader("Facturas Listas para Liberación")
    st.table(pd.DataFrame({
        "ID": ["P-101", "P-102", "P-103", "P-104"],
        "Proveedor": ["Microsoft", "Constructora Alfa", "Energía Q.", "Seguros Global"],
        "Vencimiento": ["En 2 días", "En 5 días", "Hoy", "Vencido"],
        "Prioridad IA": ["Alta", "Alta", "Crítica", "Baja"]
    }))
    st.button("Ejecutar Pagos Seleccionados")
    