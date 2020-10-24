dicionario = {'Andrew Ayres': 6, 'Fábio Ikeda': 10, 'Fábio Kurauchi': 9, 'Raul Hage': 8}
def medias_por_inicial(dicionario):
    dicionario_novo = {}
    dicionario_final = {}
    for nome,notas in dicionario.items():
            inicial = nome[0]
            if inicial not in dicionario_novo.keys():
                dicionario_novo[inicial] = [notas]
            else:
                dicionario_novo[inicial].append(notas)
    for inicio in dicionario_novo:
        valores = dicionario_novo[inicio]
        i = 0
        s = 0
        while i <len(valores):
            s+=valores[i]
            i+=1
        media = s/i
        dicionario_final[inicio]=media
    return dicionario_final
print(medias_por_inicial(dicionario))