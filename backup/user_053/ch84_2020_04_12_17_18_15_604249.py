# Define função
def inverte_dicionario(dicionario):
    # Cria dicionário de retorno
    dicionario_invertido = {}
    # Varre nomes e idades do dicionário
    for nome, idades in dicionario.items():
        # Adiciona idade no dicionário e cria lista que recebe os nomes
        if idades not in dicionario_invertido.keys():
            lista = []
            lista.append(nome)
            dicionario_invertido[idades] = lista
        # Adiciona o nome à respectiva idade já existente
        else:
            for idades_chaves, lista in dicionario_invertido.items():
                if idades == idades_chaves:
                    lista.append(nome)
    # Retorna dicionário pedido
    return dicionario_invertido