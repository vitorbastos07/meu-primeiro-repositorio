from funcoes import imprime_cartela
from funcoes import guardar_dado
from funcoes import remover_dado
from funcoes import calcula_pontos_regra_simples
from funcoes import calcula_pontos_soma
from funcoes import calcula_pontos_sequencia_baixa
from funcoes import calcula_pontos_sequencia_alta
from funcoes import calcula_pontos_full_house
from funcoes import calcula_pontos_quadra
from funcoes import calcula_pontos_quina
from funcoes import calcula_pontos_regra_avancada
from funcoes import faz_jogada
from random import randint

def rolar_dados(n):
    return [randint(1, 6) for _ in range(n)]

cartela = {
    'regra_simples': {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1},
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

imprime_cartela(cartela)

todascat = ['1', '2', '3', '4', '5', '6', 'sem_combinacao', 'quadra', 'full_house', 'sequencia_baixa', 'sequencia_alta', 'cinco_iguais']
categorias = []
i = 0

while i < 12:
    n = 5
    rolados = rolar_dados(n)
    guardados = []
    print('Dados rolados:', rolados)
    print('Dados guardados:', guardados)
    print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
    resposta = input(">")
    a = 0

    while resposta != '0':
        if resposta == '1':
            print("Digite o índice do dado a ser guardado (0 a {}):".format(len(rolados) - 1))
            indice = int(input(">"))
            while indice >= len(rolados):
                print("Índice inválido. Digite novamente:")
                indice = int(input(">"))
            resultado = guardar_dado(rolados, guardados, indice)
            rolados, guardados = resultado

        elif resposta == '2':
            print("Digite o índice do dado a ser removido (0 a {}):".format(len(guardados) - 1))
            indice_remover = int(input(">"))
            while indice_remover >= len(guardados):
                print("Índice inválido. Digite novamente:")
                indice_remover = int(input(">"))
            resultado = remover_dado(rolados, guardados, indice_remover)
            rolados, guardados = resultado

        elif resposta == '3':
            if a == 2:
                print("Você já usou todas as rerrolagens.")
            else:
                a += 1
                rolados = rolar_dados(len(rolados))

        elif resposta == '4':
            imprime_cartela(cartela)

        else:
            print("Opção inválida. Tente novamente.")

        print('Dados rolados:', rolados)
        print('Dados guardados:', guardados)
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        resposta = input(">")

    print("Digite a combinação desejada:")
    categoria = input(">")

    while categoria in categorias or categoria not in todascat:
        if categoria in categorias:
            print("Essa combinação já foi utilizada. Digite outra:")
        else:
            print("Combinação inválida. Tente novamente:")
        categoria = input(">")

    categorias.append(categoria)
    dados_finais = rolados + guardados
    cartela = faz_jogada(dados_finais, categoria, cartela)
    i += 1

imprime_cartela(cartela)

soma = 0
for tipo in cartela.values():
    for valor in tipo.values():
        soma += int(valor)

soma_simples = sum(cartela['regra_simples'].values())
if soma_simples >= 63:
    soma += 35

print("Pontuação total:", str(soma))