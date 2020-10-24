def mais_frequente(lista):
    contagem={}
    for palavra in lista:
        if not palavra in contagem:
            contagem[palavra]=1
        else:
            contagem[palavra]+=1
    maiorc=0
    maior=0
    for c,v in contagem:
        if maior<v:
            maior=v
            maiorc=c
    return maiorc
   