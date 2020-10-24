def agrupa_por_idade(p):
    nome=list(p.keys())
    idade=list(p.values())
    cria=[]
    adol=[]
    adul=[]
    idos=[]
    t=0
    for i in idade:
        if i<=11:
            cria.append(nome[t])
        elif  11<i<18:
            adol.append(nome[t])
        elif 17<i<60:
            adul.append(nome[t])
        else:
            idos.append(nome[t])
        t+=1
    dicio={'criança':cria,'adolescente':adol,'adulto':adul,'idoso':idos}
    return dicio
        
            