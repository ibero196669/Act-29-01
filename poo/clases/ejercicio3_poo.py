class Ejercicio3():
    def __init__(self):
        self.m = 0
        self.km = 0

    def leerDatos(self):
        self.m = float(input("millas= "))

    def realizarCalculo(self):
        self.km = self.m * 1.609344

    def mostrarResultado(self):
        print("km =", self.km)
