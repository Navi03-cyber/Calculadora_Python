seguir = True

while seguir:
    eleccion = input("¿Quieres sumar, restar, multiplicar o dividir? ")
    if eleccion != "sumar" or eleccion != "restar" or eleccion != "multiplicar" or eleccion != "dividir":
        print("no es una operacion válida")
        continue#omite todo el codigo de abajo y vuelve a empezar

    n1 = float(input("Dime el primer número: "))
    n2 = float(input("Y el segundo número: "))

    if eleccion == "sumar":
        resultado = n1+n2
    elif eleccion == "restar":
        resultado = n1-n2
    elif eleccion == "multiplicar":
        resultado = n1*n2
    elif eleccion == "dividir":
        if n2 != 0:
            resultado = n1/n2
        else:
            print("No puedes dividir entre cero")
            continue

    print("Resultado:", resultado)

    temp = input("¿Quieres hacer algún cálculo más? (si/no) ")
    if temp.lower() == "no":#lower convierte la cadena str en minuscula
        seguir = False