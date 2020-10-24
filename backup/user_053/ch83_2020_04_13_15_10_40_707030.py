# Define função pedida
def medias_por_inicial(dicionario):
    # Cria dicionários
    acumula_iniciais = {}   # Dicionário que conta as repetições de cada letra
    soma_notas = {}         # Dicionário que soma as notas para cada letra
    iniciais_medias = {}    # Dicionário de retorno
    # Verifica cada chave e valor do dicionário de entrada
    for nome, nota in dicionario.items():
        # Cria itens se a inicial ainda não foi contada e contabiliza quantidade e a nota
        if nome[0] not in acumula_iniciais:
           acumula_iniciais[nome[0]] = 1
           soma_notas[nome[0]] = nota
        # Acrescenta inicial repetida à quantidade já contada e soma nota dela às outras iguais
        else:
            acumula_iniciais[nome[0]] += 1
            soma_notas[nome[0]] += nota
    # Calcula média de cada inicial - As chaves das duas listas são iguais, por isso não precisa identificar
    for inicial in acumula_iniciais:
        iniciais_medias[inicial] = soma_notas[inicial]/acumula_iniciais[inicial]
    # Retorna dicionário pedido
    return iniciais_medias