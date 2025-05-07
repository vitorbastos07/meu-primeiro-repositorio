def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    valor = dados_rolados[dado_para_guardar]
    dados_rolados.pop(dado_para_guardar)
    dados_no_estoque.append(valor)
    return [dados_rolados, dados_no_estoque]

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

    for quantidade in contagem.values():
        if quantidade >= 4:
            soma = 0
            for valor in lista:
                soma += valor
            return soma
    return 0

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

def calcula_pontos_regra_avancada(lista):
    return {
        'cinco_iguais': calcula_pontos_quina(lista),
        'full_house': calcula_pontos_full_house(lista),
        'quadra': calcula_pontos_quadra(lista),
        'sem_combinacao': calcula_pontos_soma(lista),
        'sequencia_alta': calcula_pontos_sequencia_alta(lista),
        'sequencia_baixa': calcula_pontos_sequencia_baixa(lista)
    }

def faz_jogada(dados, categoria, cartela_de_pontos):
    if str(categoria) in ['1', '2', '3', '4', '5', '6']:
        categoria_num = int(categoria)
        pontos = calcula_pontos_regra_simples(dados)[categoria_num]
        cartela_de_pontos['regra_simples'][categoria_num] = pontos
    else:
        pontos = calcula_pontos_regra_avancada(dados)[categoria]
        cartela_de_pontos['regra_avancada'][categoria] = pontos
    return cartela_de_pontos

def imprime_cartela(cartela):
    print("Cartela de Pontos:")
    print("-"*25)    
    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        if cartela['regra_simples'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_simples'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    for i in cartela['regra_avancada'].keys():
        filler = " " * (15 - len(str(i)))
        if cartela['regra_avancada'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_avancada'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    print("-"*25)