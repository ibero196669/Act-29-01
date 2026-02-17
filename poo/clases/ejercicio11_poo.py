class Ejercicio11():
    def __init__(self):
        self.num = 0
        self.series = []

    def leerDatos(self):
        print("Programa que genera la serie Fibonacci")
        self.num = int(input("Ingrese un número para la serie Fibonacci: "))

    def realizarCalculo(self):
        self.series = []
        a, b = 0, 1
        while a <= self.num:
            self.series.append(a)
            a, b = b, a + b

    def mostrarResultado(self):
        print("Serie Fibonacci hasta el número", self.num, ":", self.series)

