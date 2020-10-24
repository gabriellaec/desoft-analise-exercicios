def calcula_tempo(dicionario):
    novo={}
    nomes=[]
    listaa=[]
    for a in dicionario.values():
        listaa.append((200/a)**(1/2))
    for nome in dicionario:
        nomes.append(nome)
    i=0
    while i<len(listaa):
        novo[nomes[i]]=listaa[i]
        i+=1
    return novo
