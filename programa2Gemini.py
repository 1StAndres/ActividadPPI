# El siguiente codigo fue realizado usando la ia gemini
import streamlit as st
import re

def validar_nombre(nombre):
    patron = r"^[A-Z][a-zA-Z]+$"
    return re.match(patron, nombre)

def validar_email(email):
    patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(patron, email)

def validar_telefono(telefono):
    # Permite diferentes formatos de números de teléfono (con o sin código de país, con o sin separadores)
    patron = r"^\+?(\d{2})?[-.\s]?\d{3}[-.\s]?\d{7}$"
    return re.match(patron, telefono)

def validar_fecha(fecha):
    # Puedes ajustar este patrón según el formato de fecha que desees validar
    patron = r"^\d{2}-\d{2}-\d{4}$"  # Formato DD-MM-AAAA
    return re.match(patron, fecha)

# Interfaz de usuario con Streamlit
st.title("Formulario de Validación")

nombre = st.text_input("Ingrese su nombre:")
email = st.text_input("Ingrese su correo electrónico:")
telefono = st.text_input("Ingrese su número de teléfono:")
fecha = st.text_input("Ingrese su fecha de nacimiento (DD-MM-AAAA):")

if st.button("Validar"):
    if validar_nombre(nombre):
        st.success("Nombre válido.")
    else:
        st.error("Nombre inválido. Debe comenzar con mayúscula y contener solo letras.")

    if validar_email(email):
        st.success("Correo electrónico válido.")
    else:
        st.error("Correo electrónico inválido.")

    if validar_telefono(telefono):
        st.success("Número de teléfono válido.")
    else:
        st.error("Número de teléfono inválido.")

    if validar_fecha(fecha):
        st.success("Fecha válida.")
    else:
        st.error("Fecha inválida. Debe tener el formato DD-MM-AAAA.")
