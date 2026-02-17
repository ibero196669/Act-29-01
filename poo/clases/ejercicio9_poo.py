class Ejercicio9():
    def __init__(self):
        self.cantidad = 0
        self.interes = 0
        self.anos = 0
        self.capital_anual = []

    def leerDatos(self):
        self.cantidad = float(input("¿Cantidad a invertir? "))
        self.interes = float(input("¿Interés anual (en porcentaje)? "))
        self.anos = int(input("¿Número de años? "))

    def realizarCalculo(self):
        interes_decimal = self.interes / 100
        self.capital_anual = []
        capital = self.cantidad
        for i in range(1, self.anos + 1):
            capital = capital * (1 + interes_decimal)
            self.capital_anual.append((i, capital))

    def mostrarResultado(self):
        for año, capital in self.capital_anual:
            print(f"Capital tras el año {año}: {capital:.2f}")

