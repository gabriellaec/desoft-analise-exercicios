
def mais_frequente(lista):
    maior=0
    nome=0
    dicio={}
    for palavra in lista:
        if palavra in dicio:
            dicio[palavra]+=1
        else:
            dicio[palavra]=1
    for k,v in dicio.items():
        if v>maior:
            maior=v
            nome=k
    return nome