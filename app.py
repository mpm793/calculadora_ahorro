import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Calculadora de Ahorro", page_icon="💰")

st.title("💰 Calculadora para Ahorrar una Meta")

# Entrada de datos
monto = st.number_input("¿Cuánto dinero quieres ahorrar?", min_value=1, step=1)

fecha_obj = st.date_input("¿Para qué fecha quieres reunir el dinero?", min_value=datetime.today()).strftime("%d/%m/%Y")
frecuencia = st.selectbox("¿Con qué frecuencia puedes aportar?", ["Diario", "Semanal", "Quincenal", "Mensual"]).lower()

periodo = ""
if monto:
    fecha_obj = datetime.strptime(fecha_obj, "%d/%m/%Y")
    dias_totales = (fecha_obj - datetime.now()).days

    if dias_totales <= 0:
        st.error("La fecha debe ser en el futuro.")
    else:
        if frecuencia == "diario":
            tiempo = dias_totales
            periodo = "dias"
        elif frecuencia == "semanal":
            tiempo = dias_totales / 7
            periodo = "semanas"
        elif frecuencia == "quincenal":
            tiempo = dias_totales / 15
            periodo = "quincenas"
        elif frecuencia == "mensual":
            tiempo = dias_totales / 30.44
            periodo = "meses"
        else:
            st.error("Frecuencia no válida")
            tiempo = 0

        if tiempo > 0:
            ahorro_por_periodo = monto / tiempo
            st.markdown(
                f"""
                        ### Resultado 🧮  
                        Para ahorrar **${monto:,.2f}**, necesitas aportar aproximadamente:  
                        ### 💵 ${ahorro_por_periodo:,.2f} por {round(tiempo)} {periodo}".
                        """
            )
