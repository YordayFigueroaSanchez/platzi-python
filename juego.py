#juego
import random


def run():
    numero_aleatorio = random.randint(1,100)
    numero_elegido = int(input("del 1 al 100"))
    while numero_aleatorio != numero_elegido:
        if numero_aleatorio > numero_elegido:
            print("precisas un numero mayor")
        else:
            print("precisas un numero menor")
        numero_elegido = int(input("entre el numero"))
    print("Ganaste!!!!")


if __name__ == '__main__':
    run()