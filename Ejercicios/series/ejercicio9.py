def ejercicio_9():
    cantidad = float(input("¿Cantidad a invertir? "))
    interes = float(input("¿Interés anual (en porcentaje)? "))
    anos = int(input("¿Número de años? "))

    interes_decimal = interes / 100

    for i in range(1, anos + 1):
        cantidad = cantidad * (1 + interes_decimal)
        print(f"Capital tras el año {i}: {cantidad:.2f}")