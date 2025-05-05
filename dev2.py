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