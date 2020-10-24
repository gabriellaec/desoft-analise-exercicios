# Define função
def inverte_dicionario(dicionario):
    # Cria dicionário de retorno
    dicionario_invertido = {}
    for nome, idades in dicionario.items():
        if idades not in dicionario_invertido.keys():
            lista = []
            lista.append(nome)
            dicionario_invertido[idades] = lista
        else:
            for idades_chaves, lista in dicionario_invertido.items():
                if idades == idades_chaves:
                    lista.append(nome)
    return dicionario_invertido