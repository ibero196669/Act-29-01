class Ejercicio5():
    def __init__(self):
        self.gal = 0
        self.L = 0

    def leerDatos(self):
        self.gal = float(input("Galones = "))

    def realizarCalculo(self):
        self.L = self.gal * 3.7854

    def mostrarResultado(self):
        print("Litros =", self.L)
