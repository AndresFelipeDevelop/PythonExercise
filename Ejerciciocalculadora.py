print("calculadora") 
print("Hola!, bienvenido a la calculadora") 
print("en que te puedo ayudar?")
print (1, "suma")
print (2, "resta")
print (3, "multiplicacion")
print (4, "division")
print ("puedes elegir entre las opciones 1, 2, 3 o 4 abajo!")

if __name__ == "__main__":
    opcion = int(input("Elige una opcion: "))
    if opcion == 1:
        print("Has elegido suma")
        a = float(input("Introduce el primer numero: "))
        b = float(input("Introduce el segundo numero: "))
        print("Tu resultado es...:", a + b)
    elif opcion == 2:
        print("Has elegido resta")
        a = float(input("Introduce el primer numero: "))
        b = float(input("Introduce el segundo numero: "))
        print("Tu resultado es...:", a - b)
    elif opcion == 3:
        print("Has elegido multiplicacion")
        a = float(input("Introduce el primer numero: "))
        b = float(input("Introduce el segundo numero: "))
        print("Tu resultado es...:", a * b)
    elif opcion == 4:
        print("Has elegido division")
        a = float(input("Introduce el primer numero: "))
        b = float(input("Introduce el segundo numero: "))
        if b != 0:
            print("Tu resultado es...:", a / b)
        else:
            print("Error: Division por cero")
    else:
        print("Opcion no valida")
print("Gracias por usar la calculadora")
print("Hasta luego!")
print ("recuerda, puedes volver a usar la calculadora cuando quieras")