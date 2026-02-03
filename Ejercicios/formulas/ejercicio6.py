def ejercicio_6():
    num=float(input("Escriba un número: "))
    num2=float(input("Escriba otro número: "))
    if num>num2:
        distancia=num-num2
    else:
        distancia=num2-num
        print("La distancia entre",num,"y",num2,"es",distancia)