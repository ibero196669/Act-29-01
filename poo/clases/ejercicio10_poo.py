class Ejercicio10():
    def __init__(self):
        self.altura = 0
        self.triangulo = []

    def leerDatos(self):
        self.altura = int(input("Introduce la altura del triángulo: "))

    def realizarCalculo(self):
        self.triangulo = ["0" * i for i in range(1, self.altura + 1)]

    def mostrarResultado(self):
        for fila in self.triangulo:
            print(fila)

