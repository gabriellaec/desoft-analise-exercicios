def agrupa_por_idade(nome):
    faixa={}
    crianca=[]
    ado=[]
    adul=[]
    ido=[]
    for i in nome:
        if nome[i]<=11:
            crianca.append(i)
        elif nome[i]>=12 and nome[i]<=17:
            ado.append(i)
        elif nome[i]>=18 and nome[i]<=59:
            adul.append(i)
        else:
            ido.append(i)
    faixa['crianca']=crianca
    faixa['adolescente']=ado
    faixa['adulto']=adult
    faixa['idoso']=ido