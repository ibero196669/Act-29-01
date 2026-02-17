class Ejercicio6():
    def __init__(self):
        self.num = 0
        self.num2 = 0
        self.distancia = 0

    def leerDatos(self):
        self.num = float(input("Escriba un número: "))
        self.num2 = float(input("Escriba otro número: "))

    def realizarCalculo(self):
        if self.num > self.num2:
            self.distancia = self.num - self.num2
        else:
            self.distancia = self.num2 - self.num

    def mostrarResultado(self):
        print("La distancia entre", self.num, "y", self.num2, "es", self.distancia)

