# el siguiente codigo fue creado usando la ia gemini
import streamlit as st
import re
import random

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

    return es_segura

def generar_sugerencia():
    sugerencias = [
        "Incluye al menos un número.",
        "Agrega una letra mayúscula.",
        "Utiliza una letra minúscula.",
        "Incorpora un carácter especial.",
        "Aumenta la longitud de la contraseña.",
        "Combina diferentes tipos de caracteres.",
    ]
    return random.choice(sugerencias)

# Interfaz de usuario con Streamlit
st.title("Evaluador de Contraseñas")

contrasena = st.text_input("Ingrese su contraseña:")

if contrasena:
    es_segura = evaluar_contrasena(contrasena)
    if es_segura:
        st.success("¡Excelente! Tu contraseña es muy segura.")
    else:
        st.error("Tu contraseña no es lo suficientemente segura.")
        st.info(generar_sugerencia())
