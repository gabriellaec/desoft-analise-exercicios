def mais_frequente(lista):
    dm = {}
    for i in lista:
        if i not in dm:
            dm[i] = 1 
        else: 
            dm[i] +=1
    maior_repeticao = 0
    Palavra_mais_frequente = ''
    for palavra, repeticao in dm.items():
        if  repeticao >  maior_reticao:
             maior_repeticao =  repeticao
            Palavra_mais_frequente = palavra
    return Palavra_mais_frequente