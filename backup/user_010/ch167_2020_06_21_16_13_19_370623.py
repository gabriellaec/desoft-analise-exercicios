def bairro_mais_custoso (dic):
    dic2={}
    maior=0
    mbairro=0
    for bairro,lista in dic.items():
        novalista=[]
        for i in range (6,12):
            novalista.append (lista[i])
        gasto=sum (novalista)
        dic2[bairro]=gasto
    for bairro,gasto in dic2.items():
        if gasto>maior:
            maior=gasto
            mbairro=bairro
    return mbairro