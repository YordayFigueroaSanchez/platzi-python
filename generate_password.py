#generate_password
import random


def generar_contrasenna():
    mayusculas = ['A','S','D','F','G','H']
    minusculas = ['a','s','d','f','g','h']
    simbolos = ['!','"','#','$','&']
    numeros = ['1','2','3','4','5']
    caracteres = mayusculas + minusculas + simbolos + numeros
    contrasenna = []
    for i in range(15):
        char_random = random.choice(caracteres)
        contrasenna.append(char_random)
    contrasenna = "".join(contrasenna)
    return contrasenna


def run():
    password = generar_contrasenna()
    print("tu nueva contrasenna es : " + password)
    

if __name__ == '__main__':
    run()