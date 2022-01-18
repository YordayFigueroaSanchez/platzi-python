menu = """
Conversor de monedas a:
1 - pesos cubanos
2 - pesos uru
"""
opcion = int(input(menu))
if opcion == 1:
    pesos = input("Cuantos pesos :")
    pesos = float(pesos)
    valor_dolar = 80
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes  : " + dolares)
elif opcion == 2:
    pesos = input("Cuantos pesos :")
    pesos = float(pesos)
    valor_dolar = 45
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes  : " + dolares)
else:
    print("opcion incorrecta")