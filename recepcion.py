import streamlit as st
import time
import pandas as pd

def show_recepcion():
    st.header("📥 Recepción de Documentos y Validación OCR")
    st.info("Perfil: Analista de Cuentas por Pagar")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Carga de Archivos")
        uploaded_file = st.file_uploader("Arrastra facturas PDF o XML", type=["pdf", "xml"])
        if uploaded_file:
            with st.spinner('IA analizando documento...'):
                time.sleep(2)
                st.success("Extracción completada")
                st.json({
                    "Proveedor": "Amazon Web Services",
                    "RUT": "76.xxx.xxx-k",
                    "Monto": "$1,250.00",
                    "Confianza": "98.5%"
                })

    with col2:
        st.subheader("Bandeja de Validación")
        data_ocr = pd.DataFrame({
            "Documento": ["FAC-802", "FAC-805", "NC-102"],
            "Proveedor": ["Suzuki", "Ionos Cloud", "Papelería Local"],
            "Confianza IA": ["99%", "95%", "54%"],
            "Estado": ["Validado", "Validado - Lista Blanca", "Revisión Requerida"]
        })
        st.dataframe(data_ocr, use_container_width=True)
        st.button("Procesar Lote Automático")
