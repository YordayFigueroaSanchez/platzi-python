#funciones
#def imprimir_mensaje():
#    print("mensaje en funcion")

#imprimir_mensaje()
#imprimir_mensaje()

def conversacion(mensaje):
    print("hola")
    print(mensaje)

def convertir(tipo_pesos,valor_dolar):
    pesos = int(input("Cuantos pesos " + tipo_pesos))
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes  : " + dolares)

menu = """
Conversor de monedas a:
1 - pesos cubanos
2 - pesos uru
"""
opcion = int(input(menu))
if opcion == 1:
    convertir('colombianos',2300)
elif opcion == 2:
    convertir('cubanos',81)
else:
    conversacion(opcion)
    print("opcion incorrecta")
