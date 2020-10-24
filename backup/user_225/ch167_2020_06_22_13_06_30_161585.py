def bairro_mais_custoso(dic):
    e = 0
    novodic = {}
    maior = 0
    for i in dic:
        lista = dic[i]
        gastos = 0
        e = 1
        novalista = []
        while e<len(lista):
            k = lista[-e]
            novalista.append(k)
            if e == 6:
                break
            e+=1
        e = 0
        while e<len(novalista):
            gastos+=novalista[e]
            print(gastos)
            e+=1
        novodic[i]=gastos
        for i in novodic:
            if novodic[i]>maior:
                maior = i
    return maior