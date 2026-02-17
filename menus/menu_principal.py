from Ejercicios.formulas.ejercicio1 import ejercicio_1
from Ejercicios.formulas.ejercicio2 import ejercicio_2
from Ejercicios.conversiones.ejercicio3 import ejercicio_3
from Ejercicios.conversiones.ejercicio4 import ejercicio_4
from Ejercicios.conversiones.ejercicio5 import ejercicio_5
from Ejercicios.formulas.ejercicio6 import ejercicio_6
from Ejercicios.series.ejercicio7 import ejercicio_7
from Ejercicios.series.ejercicio8 import ejercicio_8
from Ejercicios.series.ejercicio9 import ejercicio_9
from Ejercicios.series.ejercicio10 import ejercicio_10
from Ejercicios.series.ejercicio11 import ejercicio_11

from poo.clases.ejercicio1_poo import Ejercicio1
from poo.clases.ejercicio2_poo import Ejercicio2
from poo.clases.ejercicio3_poo import Ejercicio3
from poo.clases.ejercicio4_poo import Ejercicio4
from poo.clases.ejercicio5_poo import Ejercicio5
from poo.clases.ejercicio6_poo import Ejercicio6
from poo.clases.ejercicio7_poo import Ejercicio7
from poo.clases.ejercicio8_poo import Ejercicio8
from poo.clases.ejercicio9_poo import Ejercicio9
from poo.clases.ejercicio10_poo import Ejercicio10
from poo.clases.ejercicio11_poo import Ejercicio11

def menu_principal():
    while True:
        print("Menú principal")
        print("1. Ejercicio 1")
        print("2. Ejercicio 2")
        print("3. Ejercicio 3")
        print("4. Ejercicio 4")
        print("5. Ejercicio 5")
        print("6. Ejercicio 6")
        print("7. Ejercicio 7")
        print("8. Ejercicio 8")
        print("9. Ejercicio 9")
        print("10. Ejercicio 10")
        print("11. Ejercicio 11")
        print("12. Salir")
        op=int(input("Eliga una opción: "))
        match(op):
            case 1:
                #ejercicio_1()
                ejercicio = Ejercicio1()
                ejercicio.leerDatos()
                ejercicio.realizarCalculo()
                ejercicio.mostrarResultado()
            case 2:
                #ejercicio_2()
                ejercicio = Ejercicio2()
                ejercicio.leerDatos()
                ejercicio.realizarCalculo()
                ejercicio.mostrarResultado()
            case 3:
                #ejercicio_3()
                ejercicio = Ejercicio3()
                ejercicio.leerDatos()
                ejercicio.realizarCalculo()
                ejercicio.mostrarResultado()
            case 4:
                #ejercicio_4()
                ejercicio = Ejercicio4()
                ejercicio.leerDatos()
                ejercicio.realizarCalculo()
                ejercicio.mostrarResultado()
            case 5:
                #ejercicio_5()
                ejercicio = Ejercicio5()
                ejercicio.leerDatos()
                ejercicio.realizarCalculo()
                ejercicio.mostrarResultado()
            case 6:
                #ejercicio_6()
                ejercicio = Ejercicio6()
                ejercicio.leerDatos()
                ejercicio.realizarCalculo()
                ejercicio.mostrarResultado()
            case 7:
                #ejercicio_7()
                ejercicio = Ejercicio7()
                ejercicio.leerDatos()
                ejercicio.realizarCalculo()
                ejercicio.mostrarResultado()
            case 8:
                #ejercicio_8()
                ejercicio = Ejercicio8()
                ejercicio.leerDatos()
                ejercicio.realizarCalculo()
                ejercicio.mostrarResultado()
            case 9:
                #ejercicio_9()
                ejercicio = Ejercicio9()
                ejercicio.leerDatos()
                ejercicio.realizarCalculo()
                ejercicio.mostrarResultado()
            case 10:
                #ejercicio_10()
                ejercicio = Ejercicio10()
                ejercicio.leerDatos()
                ejercicio.realizarCalculo()
                ejercicio.mostrarResultado()

            case 11:
                #ejercicio_11()
                ejercicio = Ejercicio11()
                ejercicio.leerDatos()
                ejercicio.realizarCalculo()
                ejercicio.mostrarResultado()
            case 12:
                break
            case _:
                print("Opción no válida")