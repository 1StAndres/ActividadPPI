#El siguiente programa fue creado usando la ia gemini
import streamlit as st
import pandas as pd
import re
import csv
import io

def procesar_csv(archivo_csv):
    """Procesa un archivo CSV y extrae información utilizando expresiones regulares.

    Args:
        archivo_csv (io.TextIOWrapper): Archivo CSV cargado.

    Returns:
        pandas.DataFrame: DataFrame con los datos extraídos.
    """
    datos = []
    lector = csv.reader(archivo_csv)
    for fila in lector:
        try:
            # Ajusta los índices y patrones regex según tu CSV
            numero_serie = re.search(r"^\d+", fila[0]).group() if re.search(r"^\d+", fila[0]) else ""
            nombre_producto = re.search(r"[A-Za-z\s]+", fila[1]).group() if re.search(r"[A-Za-z\s]+", fila[1]) else ""
            valor = re.search(r"\d+\.\d{2}", fila[2]).group() if re.search(r"\d+\.\d{2}", fila[2]) else ""
            fecha = re.search(r"\d{2}/\d{2}/\d{2}", fila[3]).group() if re.search(r"\d{2}/\d{2}/\d{2}", fila[3]) else ""

            info_contacto = fila[4] if len(fila) > 4 else ""
            nombre = re.search(r"[A-Z][a-z]+", info_contacto).group() if re.search(r"[A-Z][a-z]+", info_contacto) else ""
            email = re.search(r"\S+@\S+", info_contacto).group() if re.search(r"\S+@\S+", info_contacto) else ""
            telefono = re.search(r"\d{10}", info_contacto).group() if re.search(r"\d{10}", info_contacto) else ""

            datos.append([numero_serie, nombre_producto, valor, fecha, nombre, email, telefono])
        except IndexError:
            continue  # Si la fila no tiene suficientes columnas, la omitimos

    return pd.DataFrame(datos, columns=["Número de Serie", "Nombre Producto", "Valor", "Fecha", "Nombre", "Email", "Teléfono"])

# Interfaz de usuario de Streamlit
st.title("Procesador de CSV a Excel")

uploaded_file = st.file_uploader("Sube tu archivo CSV", type="csv")

if uploaded_file is not None:
    archivo_texto = io.TextIOWrapper(uploaded_file, encoding="utf-8")
    datos = procesar_csv(archivo_texto)
    st.dataframe(datos)

    # Descargar el DataFrame como un archivo Excel
    buffer = io.BytesIO()
    datos.to_excel(buffer, index=False, engine='openpyxl')
    buffer.seek(0)

    st.download_button(
        label="Descargar como Excel",
        data=buffer,
        file_name="productos.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

