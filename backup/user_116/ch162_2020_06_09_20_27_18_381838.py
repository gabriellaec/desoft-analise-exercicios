def verifica_lista(lista):
    x=len(lista)
    listap=[]
    listai=[]
    for v in lista:
        if v%2==0:
            listap.append(v)
        elif v% 2!=0:
            listai.append(v)

    if len(listap)==x and x!=0:
        return 'par'

    elif len(listai)==x and x!=0: 
        return 'ímpar'

    elif len(listai)!=x and len(listap)!=x or x==0:
        return 'misturado'