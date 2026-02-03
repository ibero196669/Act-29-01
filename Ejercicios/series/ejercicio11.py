def ejercicio_11():
    print("Programa que genera la serie Fibonacci")
    num = int(input("Ingrese un número para la serie Fibonacci: "))

    a, b = 0, 1
    series = []
    while a <= num:
        series.append(a)
        a, b = b, a + b

    print("Serie Fibonacci hasta el número", num, ":", series)