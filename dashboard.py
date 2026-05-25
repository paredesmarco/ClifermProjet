import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

def show_dashboard():
    # Configuración de la página
    st.set_page_config(page_title="ClifermProjet IA - Dashboard", layout="wide")

    # --- TÍTULO Y ESTADO DEL MODELO ---
    st.title("📊 ClifermProjet IA: Gestión de Cuentas por Pagar")
    st.markdown("---")

    # --- INDICADORES PRINCIPALES (KPIs) ---
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(label="Confianza del Modelo", value="92.2%", delta="1.5% ⬆️")
    with col2:
        st.metric(label="Tasa de Automatización (STP)", value="85%", delta="5% ⬆️")
    with col3:
        st.metric(label="Ahorro Operativo (Mensual)", value="$15,500", delta="$2,100 ⬆️")
    with col4:
        st.metric(label="Tiempo Promedio Proceso", value="12 min", delta="-4h ⬇️", delta_color="normal")

    st.markdown("---")

    # --- SECCIÓN VISUAL (GRÁFICOS) ---
    col_left, col_right = st.columns(2)

    with col_left:
        st.subheader("Eficiencia: Humano vs. ClifermProjet IA")
        # Datos simulados para el gráfico de barras
        data_eficiencia = pd.DataFrame({
            'Método': ['Manual (Antes)', 'IA (Ahora)'],
            'Minutos por Factura': [240, 12]
        })
        fig_bar = px.bar(data_eficiencia, x='Método', y='Minutos por Factura', color='Método', 
                        color_discrete_sequence=['#FF4B4B', '#00CC96'])
        st.plotly_chart(fig_bar, use_container_width=True)

    with col_right:
        st.subheader("Distribución de Documentos")
        # Datos simulados para el gráfico de dona
        data_docs = pd.DataFrame({
            'Estado': ['Aprobado Auto', 'Revisión Humana', 'Rechazado'],
            'Cantidad': [850, 120, 30]
        })
        fig_pie = px.pie(data_docs, values='Cantidad', names='Estado', hole=0.5,
                        color_discrete_sequence=['#00CC96', '#FFA15A', '#EF553B'])
        st.plotly_chart(fig_pie, use_container_width=True)

    st.markdown("---")

    # --- SECCIÓN VISUAL 2: LIQUIDEZ Y ERRORES OCR (NUEVOS GRÁFICOS) ---
    col_c, col_d = st.columns(2)

    with col_c:
        st.subheader("💰 Top Proveedores Pendientes")
        # Datos simulados de montos altos por pagar
        data_liq = pd.DataFrame({
            'Proveedor': ['Microsoft Azure', 'Constructora Alfa', 'Energía Eléctrica Q.', 'Seguros Global', 'Logística Express'],
            'Monto Pendiente ($)': [12500, 9800, 7500, 5200, 3100]
        }).sort_values('Monto Pendiente ($)', ascending=True)
        
        fig_liq = px.bar(data_liq, y='Proveedor', x='Monto Pendiente ($)', orientation='h',
                        color='Monto Pendiente ($)', color_continuous_scale='Blues',
                        text_auto='.2s')
        st.plotly_chart(fig_liq, use_container_width=True)

    with col_d:
        st.subheader("🔍 Errores Comunes")
        # Datos actualizados: Se elimina 'Recibo Manual'
        tipos_doc = ['Factura PDF', 'Nota Crédito', 'XML SII']
        tipos_error = ['RUT Ilegible', 'Monto Difuso', 'Fecha Inválida', 'Firma Faltante']
        
        # Matriz de errores ajustada (se eliminó la fila correspondiente a Recibo Manual)
        z = [
            [15, 5, 2, 8],  # Factura PDF
            [2, 12, 1, 4],  # Nota Crédito
            [0, 2, 1, 0]     # XML SII
        ]
        
        fig_heat = px.imshow(z, x=tipos_error, y=tipos_doc, 
                            labels=dict(x="Tipo de Error", y="Tipo de Documento", color="Frecuencia"),
                            color_continuous_scale='Reds', text_auto=True)
        st.plotly_chart(fig_heat, use_container_width=True)

    # --- TABLA DE DETALLE CON IA ---
    st.markdown("---")
    st.subheader("📋 Registro de Facturas Recientes (Análisis de IA)")

    # Generamos datos de ejemplo para la tabla
    data_tabla = {
        "ID Factura": ["F-8021", "F-8022", "F-8023", "F-8024"],
        "Proveedor": ["Amazon Web Services", "Arriendos S.A.", "Papelería Local", "Servicios Eléctricos"],
        "Cuenta Contable (IA)": ["Infraestructura Cloud", "Costos Operativos", "Suministros", "Servicios Básicos"],
        "Confianza IA": ["99%", "95%", "62%", "98%"],
        "Estado": ["✅ Auto-Pagado", "✅ Auto-Pagado", "⚠️ Revisión Requerida", "✅ Auto-Pagado"]
    }

    st.table(pd.DataFrame(data_tabla))

    # --- NOTA TÉCNICA ---
    st.info("**Nota del Modelo:** Las facturas con confianza menor al 70% son derivadas automáticamente al equipo de supervisión humana para validación.")
