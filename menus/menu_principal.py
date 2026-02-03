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
                ejercicio_1()
            case 2:
                ejercicio_2()
            case 3:
                ejercicio_3()
            case 4:
                ejercicio_4()
            case 5:
                ejercicio_5()
            case 6:
                ejercicio_6()
            case 7:
                ejercicio_7()
            case 8:
                ejercicio_8()
            case 9:
                ejercicio_9()
            case 10:
                ejercicio_10()
            case 11:
                ejercicio_11()
            case 12:
                break
            case _:
                print("Opción no válida")