#El siguiente codigo fue generado con la ia gemini
import streamlit as st
import pandas as pd
import re

st.title("Extractor de Información con Regex por Andres Arbelaez")

uploaded_file = st.file_uploader("Sube tu archivo de texto", type="txt")

if uploaded_file is not None:
    # Leer el archivo de texto
    text = uploaded_file.read().decode('utf-8')

    # Área para ingresar expresiones regulares
    regex_patterns = st.text_area("Ingrese sus expresiones regulares (una por línea)", height=200)
    patterns = regex_patterns.splitlines()

    # Extraer la información
    matches = []
    for pattern in patterns:
        for match in re.finditer(pattern, text):
            matches.append(match.group())

    # Mostrar resultados
    df = pd.DataFrame(matches, columns=["Coincidencias"])
    st.dataframe(df)

    # Descargar resultados
    csv = df.to_csv(index=False)
    st.download_button(
        label="Descargar como CSV",
        data=csv,
        file_name='resultados.csv',
        mime='text/csv'
    )
