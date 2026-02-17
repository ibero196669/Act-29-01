class Ejercicio1():
    def __init__(self):
        self.x = 0
        self.w = 0
        self.l = 0
        self.m = 0

    def leerDatos(self):
        print("Programa que calcula M")
        self.x = int(input("x= "))
        self.w = int(input("w= "))
        self.l = int(input("l= "))

    def realizarCalculo(self):
        self.m = self.x * self.w * (self.l - self.x) / self.l

    def mostrarResultado(self):
        print("m =", self.m)


