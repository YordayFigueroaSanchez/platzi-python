#diccionario
def run():
    mi_diccionario = {
        "llave1":1,
        "llave2":2,
        "llave3":3,
    }
    #print(mi_diccionario)

    poblacion_paises = {
        "brasil":3456783,
        "argentina":23134,
        "uruguay":1234,
    }
    for pais in poblacion_paises.keys():
        print(pais)
    for poblacion in poblacion_paises.values():
        print(poblacion)
    for pais,poblacion in poblacion_paises.items():
        print(pais + " tiene " + str(poblacion))


if __name__ == '__main__':
    run()