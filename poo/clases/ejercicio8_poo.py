class Ejercicio8():
    def __init__(self):
        self.numero = 0
        self.impares = []

    def leerDatos(self):
        self.numero = int(input("Introduce un número entero positivo: "))

    def realizarCalculo(self):
        self.impares = [i for i in range(1, self.numero + 1, 2)]

    def mostrarResultado(self):
        print(", ".join(map(str, self.impares)))


