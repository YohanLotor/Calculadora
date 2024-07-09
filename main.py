import sumar
import resta
import multiplicacion
import dividir
import suma_avanzada

def menu():
    print("Calculadora")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Dividir dos números")
    print("5. Suma avanzada de N números")
    print("6. Salir")
    return input("Seleccione una opción: ")

def main():
    while True:
        opcion = menu()
        if opcion == '1':
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print("Resultado:", sumar.sumar(a, b))
        elif opcion == '2':
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print("Resultado:", resta.restar(a, b))
        elif opcion == '3':
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print("Resultado:", multiplicacion.multiplicar(a, b))
        elif opcion == '4':
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print("Resultado:", dividir.dividir(a, b))
        elif opcion == '5':
            numeros = input("Ingrese los números separados por espacio: ").split()
            numeros = [float(num) for num in numeros]
            print("Resultado:", suma_avanzada.suma_avanzada(numeros))
        elif opcion == '6':
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()