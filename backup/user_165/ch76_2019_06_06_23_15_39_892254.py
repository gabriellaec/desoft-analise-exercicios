def aniversariantes_de_setembro(dicionario):
    novo_dicionario = {}
    Lista1 = []
    Lista2 = [] #nomes
    for nome, datas in dicionario.items():
        Lista2.append(nome)
        Lista1.append(datas)
    for i in range(len(Lista1)):
        if Lista1[i][3:5] == "09":
            novo_dicionario[Lista2[i]] = Lista1[i]
    return novo_dicionario
        