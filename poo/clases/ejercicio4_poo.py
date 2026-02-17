class Ejercicio4():
    def __init__(self):
        self.f = 0
        self.c = 0

    def leerDatos(self):
        self.f = float(input("Grados Fahrenheit = "))

    def realizarCalculo(self):
        self.c = (self.f - 32) * 5 / 9

    def mostrarResultado(self):
        print("Grados Celsius =", self.c)