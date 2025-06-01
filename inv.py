from datetime import datetime, timedelta

def calculate_savings_plan():
    """
    Calculates a savings plan based on user input for amount, target date, and frequency.
    It includes robust input validation and provides a clear savings goal.
    """
    # --- Get and validate the target savings amount ---
    while True:
        try:
            monto_str = input("¿Cuánto dinero quieres ahorrar? ")
            monto = float(monto_str) # Convert input string to a float
            if monto <= 0:
                print("El monto a ahorrar debe ser un número positivo. Por favor, inténtalo de nuevo.")
                continue
            break
        except ValueError:
            print("Entrada inválida para el monto. Por favor, introduce un número.")

    # --- Get and validate the target date ---
    while True:
        # Prompt for 4-digit year (AAAA)
        fecha_str = input("¿Para qué fecha quieres reunir el dinero (DD/MM/AAAA)? ")
        try:
            # Use %Y for 4-digit year
            fecha_objetivo = datetime.strptime(fecha_str, "%d/%m/%Y")
            if fecha_objetivo < datetime.now():
                print("La fecha objetivo no puede ser en el pasado. Por favor, introduce una fecha futura.")
                continue
            break
        except ValueError:
            # Updated error message to reflect 4-digit year
            print("Formato de fecha inválido. Por favor, usa DD/MM/AAAA (ej. 31/12/2025).")

    # --- Get and validate the saving frequency ---
    while True:
        frecuencia = input("¿Con qué frecuencia puedes aportar (diario/semanal/quincenal/mensual)? ").lower()
        if frecuencia in ["diario", "semanal", "quincenal", "mensual"]:
            break
        else:
            print("Frecuencia no válida. Por favor, elige entre 'diario', 'semanal', 'quincenal' o 'mensual'.")

    # --- Calculate the time difference and savings per period ---
    hoy = datetime.now()
    diferencia_tiempo = fecha_objetivo - hoy

    if frecuencia == "diario":
        # Calculate number of full days remaining
        periodos = diferencia_tiempo.days
        if periodos <= 0:
            print("La fecha objetivo es hoy o en el pasado. No hay tiempo para ahorrar diariamente.")
            return
        ahorro_por_periodo = monto / periodos # Correct division for calculation
        print(f"\nPara ahorrar ${monto:.2f} en {periodos} días, necesitarías ahorrar ${ahorro_por_periodo:.2f} **diariamente**.")
    elif frecuencia == "semanal":
        # Calculate number of full weeks remaining
        periodos = diferencia_tiempo.days / 7
        if periodos <= 0:
            print("No hay semanas completas entre hoy y tu fecha objetivo.")
            return
        ahorro_por_periodo = monto / periodos # Correct division for calculation
        print(f"\nPara ahorrar ${monto:.2f} en {int(periodos)} semanas, necesitarías ahorrar ${ahorro_por_periodo:.2f} **semanalmente**.")
    elif frecuencia == "quincenal":
        # Calculate number of full fortnights remaining
        periodos = diferencia_tiempo.days / 15
        if periodos <= 0:
            print("No hay quincenas completas entre hoy y tu fecha objetivo.")
            return
        ahorro_por_periodo = monto / periodos # Correct division for calculation
        print(f"\nPara ahorrar ${monto:.2f} en {int(periodos)} quincenas, necesitarías ahorrar ${ahorro_por_periodo:.2f} **quincenalmente**.")
    elif frecuencia == "mensual":
        # Approximate number of months based on average days per month
        periodos = diferencia_tiempo.days / 30.44
        if periodos <= 0:
            print("No hay meses completos entre hoy y tu fecha objetivo.")
            return
        ahorro_por_periodo = monto / periodos # Correct division for calculation
        print(f"\nPara ahorrar ${monto:.2f} en {int(periodos)} meses, necesitarías ahorrar ${ahorro_por_periodo:.2f} **mensualmente**.")

# Run the function to start the savings calculator
calculate_savings_plan()