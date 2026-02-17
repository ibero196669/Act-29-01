class Ejercicio2():
    def __init__(self):
        self.r = 0
        self.c = 0

    def leerDatos(self):
        self.r = float(input("r= "))

    def realizarCalculo(self):
        self.c = 2 * 3.14 * self.r

    def mostrarResultado(self):
        print("c =", self.c)


