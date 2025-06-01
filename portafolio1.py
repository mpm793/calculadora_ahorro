from datetime import  datetime, timedelta


monto = int(input("cuento dinero quieres ahorrar? "))
fecha_str = input("fecha que quieres reunir el dinero dd/mm/aaaa")
frecuencia=input("con que frecuenia puede aportar ahorro 'diario/semanal/quincenal/mensual'").lower()

fecha_obj = datetime.strptime(fecha_str, "%d/%m/%Y")
periods= fecha_obj-datetime.now()

tiempo = 0
cant_mensual = 0
def calculo_cantidad():
    global cant_mensual
    cant_mensual = monto/tiempo


if frecuencia == "diario":
    tiempo = periods.days
    calculo_cantidad()
    print(f"para ahorrar $ {monto:.2f} necesitas ahorrar $ {round(cant_mensual,2)} por {round(tiempo)} dias ")
elif frecuencia == "semanal":
    tiempo = periods.days/7
    calculo_cantidad()
    print(f"para ahorrar $ {monto:.2f} necesitas ahorrar $ {round(cant_mensual,2)} por {round(tiempo)} semanas ")
elif frecuencia == "quincenal":
     tiempo = periods.days/15
     calculo_cantidad()
     print(f"para ahorrar $ {monto:.2f} necesitas ahorrar $ {round(cant_mensual,2)} por {round(tiempo)} quincenas ")
elif frecuencia == "mensual":
    tiempo = periods.days/30.44
    calculo_cantidad()
    print(f"para ahorrar $ {monto:.2f} necesitas ahorrar $ {round(cant_mensual,2)} por {round(tiempo)} meses ")
else:
    print("Error en captura de datos ")




