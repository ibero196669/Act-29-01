class Ejercicio7():
    def __init__(self):
        self.palabra = ""

    def leerDatos(self):
        self.palabra = input("Introduce una palabra: ")

    def realizarCalculo(self):
        self.resultado = [self.palabra for _ in range(10)]

    def mostrarResultado(self):
        for palabra in self.resultado:
            print(palabra)

