import random

def rolar_dados(n):
    lista = []
    for _ in range(n):
        lista.append(random.randint(1, 6))
    return lista
