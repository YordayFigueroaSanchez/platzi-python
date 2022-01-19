#palindromo
def es_palindromo(palabra):
    palabra = palabra.replace(' ','')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida :
        return True
    else:
        return False
         

def run():
    palabra = input("Escribe una palabra : ")
    if es_palindromo(palabra) == True:
        print("palindromo")
    else:
        print("no es palindromo")


if __name__ == '__main__':
    run()