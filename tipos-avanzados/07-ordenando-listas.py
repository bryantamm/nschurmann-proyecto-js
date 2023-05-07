numeros = [2, 4, 5, 1, 3, 12]

# numeros.sort(reverse=True)
numeros2 = sorted(numeros, reverse=True)
print(numeros)
print(numeros2)

usuarios = [[4, "chanchito"],
            [1, "felipe"],
            [5, "pulga"]]


# def ordena(elemento):
#     return elemento[1]


usuarios.sort(key=lambda el: el[1], reverse=True)

print(usuarios)
print(usuarios)
