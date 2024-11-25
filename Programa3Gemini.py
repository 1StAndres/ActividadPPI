#El siguiente programa fue creado usando la ia gemini
import streamlit as st
import pandas as pd
import re

def procesar_csv(archivo_csv):
    """Procesa un archivo CSV y extrae información utilizando expresiones regulares.

    Args:
        archivo_csv (str): Ruta al archivo CSV.

    Returns:
        pandas.DataFrame: DataFrame con los datos extraídos.
    """

    datos = []
    with open(archivo_csv, 'r') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            # Ajusta los índices y patrones regex según tu CSV
            numero_serie = re.search(r"^\d+", fila[0]).group()
            nombre_producto = re.search(r"[A-Za-z\s]+", fila[1]).group()
            valor = re.search(r"\d+\.\d{2}", fila[2]).group()
            fecha = re.search(r"\d{2}/\d{2}/\d{2}", fila[3]).group()
            # ... y así sucesivamente para otros campos

            # Ejemplo de extracción de información de contacto en un solo campo
            info_contacto = fila[4]
            nombre = re.search(r"[A-Z][a-z]+", info_contacto).group()
            email = re.search(r"\S+@\S+", info_contacto).group()
            telefono = re.search(r"\d{10}", info_contacto).group()

            datos.append([numero_serie, nombre_producto, valor, fecha, nombre, email, telefono])

    return pd.DataFrame(datos, columns=["Número de Serie", "Nombre Producto", "Valor", "Fecha", "Nombre", "Email", "Teléfono"])

# Interfaz de usuario de Streamlit
st.title("Procesador de CSV a Excel")

uploaded_file = st.file_uploader("Sube tu archivo CSV", type="csv")

if uploaded_file is not None:
    # To go to a specific file in your directory in case you want to open a local file directly
    # uploaded_file = open('your_file.csv', 'r')
    datos = procesar_csv(uploaded_file)
    st.dataframe(datos)

    # Descargar el DataFrame como un archivo Excel
    st.download_button(
        label="Descargar como Excel",
        data=datos.to_excel(index=False, engine='openpyxl'),
        file_name='productos.xlsx',
        mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
