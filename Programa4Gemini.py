#El siguiente codigo fue generado usando la ia gemini
import streamlit as st
import pandas as pd
import re

st.title("Extractor de Información con Regex por Andres Arbelaez")

# Subir archivo de texto
uploaded_file = st.file_uploader("Sube tu archivo de texto", type="txt")

if uploaded_file is not None:
    try:
        # Leer el archivo de texto
        text = uploaded_file.read().decode('utf-8').strip()
        if not text:
            st.warning("El archivo subido está vacío. Por favor, sube un archivo con contenido.")
        else:
            # Área para ingresar expresiones regulares
            regex_patterns = st.text_area("Ingrese sus expresiones regulares (una por línea)", height=200)
            if not regex_patterns.strip():
                st.warning("Por favor, ingresa al menos una expresión regular.")
            else:
                patterns = regex_patterns.splitlines()

                # Extraer la información
                matches = []
                for pattern in patterns:
                    try:
                        for match in re.finditer(pattern.strip(), text):
                            matches.append(match.group())
                    except re.error as e:
                        st.error(f"Error en la expresión regular '{pattern}': {e}")

                # Mostrar resultados
                if matches:
                    df = pd.DataFrame(matches, columns=["Coincidencias"])
                    st.dataframe(df)

                    # Descargar resultados
                    csv = df.to_csv(index=False, encoding='utf-8')
                    st.download_button(
                        label="Descargar como CSV",
                        data=csv,
                        file_name='resultados.csv',
                        mime='text/csv'
                    )
                else:
                    st.info("No se encontraron coincidencias para las expresiones regulares proporcionadas.")
    except Exception as e:
        st.error(f"Ocurrió un error al procesar el archivo: {e}")
else:
    st.info("Sube un archivo de texto para comenzar.")

