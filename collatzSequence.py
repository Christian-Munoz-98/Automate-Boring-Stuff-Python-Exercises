import sys, os
def collatz(number):
    if number == 1:
        return 1
    if number%2 == 0:
        return number//2
    if number%2 == 1:
        return 3*number+1

def run():
    while True:
        try:
            number = int(input('Escriba un número---->'))

            print(number)

            while collatz(number) != 1:
                print(collatz(number))
                number = collatz(number)
            else:
                print(1)   
        except ValueError:
            print("Sólo puede ingresar números enteros")
        opcion_salida = input('\nSi desea salir del programa presione la tecla N\nSi desea calcular otra serie presione enter\n')
        if opcion_salida == 'N' or opcion_salida == 'n':
            sys.exit()
        os.system('cls')

if __name__ == '__main__':
    run()