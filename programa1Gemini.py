# el siguiente codigo fue creado usando la ia gemini
import streamlit as st
import re

def evaluar_contrasena(contrasena):
    # Expresiones regulares para cada criterio
    mayuscula = re.compile(r'[A-Z]')
    minuscula = re.compile(r'[a-z]')
    numero = re.compile(r'\d')
    especial = re.compile(r'[^A-Za-z0-9]')

    # Evaluar si cumple con todos los criterios
    es_segura = (
        len(contrasena) >= 8 and
        mayuscula.search(contrasena) and
        minuscula.search(contrasena) and
        numero.search(contrasena) and
        especial.search(contrasena)
    )

    # Crear un diccionario para almacenar los criterios que faltan
    criterios_faltantes = []
    if len(password) < 8:
        criterios_faltantes.append("longitud (mínimo 8 caracteres)")
    if not mayuscula.search(contrasena):
        criterios_faltantes.append("al menos una letra mayúscula")
    if not minuscula.search(contrasena):
        criterios_faltantes.append("al menos una letra minúscula")
    if not numero.search(contrasena):
        criterios_faltantes.append("al menos un número")
    if not especial.search(contrasena):
        criterios_faltantes.append("al menos un carácter especial")

    return es_segura, criterios_faltantes

# Interfaz de usuario con Streamlit
st.title("Evaluador de Contraseñas por Andres Arbelaez")

password = st.text_input("Ingrese su contraseña", type="password")

# Función para mostrar/ocultar la contraseña
def toggle_password_visibility():
    password_input = st.session_state.get('password_input')
    password_input.type = "text" if password_input.type == "password" else "password"

# Botón con icono de ojo
col1, col2 = st.columns(2)
with col1:
    st.write("")  # Espacio en blanco para alinear el botón
with col2:
    if password:
        st.button("Mostrar", on_click=toggle_password_visibility, key="toggle_password")


if password:
    es_segura, criterios_faltantes = evaluar_contrasena(password)
    if es_segura:
        st.success("¡Excelente! Tu contraseña es muy segura.")
    else:
        st.error("Tu contraseña no es lo suficientemente segura.")
        st.info("Para mejorarla, te recomendamos incluir: " + ", ".join(criterios_faltantes))
