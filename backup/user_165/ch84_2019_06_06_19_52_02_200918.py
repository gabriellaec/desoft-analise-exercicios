dicionario_1 = {'Ana': 19, 'Bruno': 18, 'João': 19}
def inverte_dicionario(dicionario_1):
    dicionario_novo = {}
    for nome,valores in dicionario_1.items():
        if valores not in dicionario_novo:
            dicionario_novo[valores] = [nome]
        else:
            dicionario_novo[valores].append[nome]
    return dicionario_novo 
print(inverte_dicionario(dicionario_1))