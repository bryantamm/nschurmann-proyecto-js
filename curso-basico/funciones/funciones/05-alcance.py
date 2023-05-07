saludo = 25
# no Çutilizar variables globales


def saludar():
    global saludo
    saludo = "hola mundo"
    # saludo = 3


def saludachanchito():
    saludo = 24
    print(saludo)


resultado1 = saludo + 3
print(resultado1)
saludar()
resultado2 = saludo + 3
print(resultado2)
