dicionario1 = {'Ana': 19, 'Bruno': 18, 'João': 19}
dicionario2 = {}
def inverte_dicionario(dicionario1):
    for value in dicionario1.values():
        dicionario2.append(value)
        for item in dicionario1.itens():
            dicionario2[value].append(item)
            return dicionario2
                           