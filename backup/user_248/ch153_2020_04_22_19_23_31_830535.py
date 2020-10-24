def agrupa_por_idade(nomes):
    faixa_etaria=dict()
    crianca=[]
    adulto=[]
    adoles=[]
    idoso=[]
    for i in nomes:
        if nomes[i]<=11:
            crianca.append(i)
        elif nomes[i]>=12 and nomes[i]<=17:
            adoles.append(i)
        elif nomes[i]>=18 and nomes[i]<=59:
            adul.append(i)
        else:
            idoso.append(i)
        faixa_etaria['criança']=crianca
        faixa_etaria['adolescente']=adoles
        faixa_etaria['adulto']=adulto
        faixa_etaria['idoso']=ido
        return faixa_etaria
                     
            
            