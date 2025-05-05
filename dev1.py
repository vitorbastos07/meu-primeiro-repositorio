import random

def rolar_dados(n):
    lista = []
    for _ in range(n):
        lista.append(random.randint(1, 6))
    return lista

def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
     valor = dados_no_estoque[dado_para_remover]
     dados_no_estoque.pop(dado_para_remover)
     dados_rolados.append(valor)
     return [dados_rolados, dados_no_estoque]


def calcula_pontos_regra_simples(lista):
    pontuacao = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for dado in lista:
        if dado in pontuacao:
            pontuacao[dado] += dado
    return pontuacao

def calcula_pontos_soma(lista):
    total = 0
    for valor in lista:
        total += valor
    return total

def calcula_pontos_sequencia_baixa(lista):
    lista_ordenada = sorted(lista)
    contador = 1
    for i in range(1, len(lista_ordenada)):
        if lista_ordenada[i] == lista_ordenada[i-1] + 1:
            contador += 1
            if contador >= 4:
                return 15
        elif lista_ordenada[i] != lista_ordenada[i-1]:
            contador = 1
    return 0

def calcula_pontos_sequencia_alta(lista):
    lista_ordenada = sorted(lista)
    contador = 1
    for i in range(1, len(lista_ordenada)):
        if lista_ordenada[i] == lista_ordenada[i-1] + 1:
            contador += 1
            if contador >= 5:
                return 30
        elif lista_ordenada[i] != lista_ordenada[i-1]:
            contador = 1
    return 0

def calcula_pontos_full_house(lista):
    contagem = {}
    for dado in lista:
        if dado in contagem:
            contagem[dado] += 1
        else:
            contagem[dado] = 1

    if sorted(contagem.values()) == [2, 3]:
        soma = 0
        for valor in lista:
            soma += valor
        return soma
    else:
        return 0
    
   def calcula_pontos_quadra(lista):
    contagem = {}
    for dado in lista:
        if dado in contagem:
            contagem[dado] += 1
        else:
            contagem[dado] = 1

def calcula_pontos_quina(lista):
    contagem = {}
    for dado in lista:
        if dado in contagem:
            contagem[dado] += 1
        else:
            contagem[dado] = 1

    for quantidade in contagem.values():
        if quantidade >= 5:
            return 50
    return 0
