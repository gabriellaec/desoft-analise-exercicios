def agrupa_por_idade(dic_n_age):
    Nome_faixa={}
    cri=[]
    ado=[]
    adu=[]
    ido=[]
    for i in dic_n_age.keys():
        if dic_nomeidade[i]<12:
            cri.append(n)
        elif 12<=dic_n_age[i]<18:
            ado.append(n)
        elif 18<=dic_n_age[i]<60:
            adu.append(i)
        else:
            ido.append(i)
       Nome_faixa['criança']= cri
       Nome_faixa['adolescente']= ado
       Nome_faixa['adulto']= adu
       Nome_faixa['idoso']= ido
    return Nome_faixa
dicionario = {'jao':10, 'maria':14, 'luiz':7}
print (agrupa_por_idade(dicionario))    
nome = dicionario.keys()
idades = dicionario.values()
print (nome)
print(idades)
print (dicionario.items())

def agrupa_por_idade(dic_nomes_e_idades):
    dic_faixa_etaria={}
    faixa_crianca=[]
    faixa_adolescente=[]
    faixa_adulto=[]
    faixa_idoso=[]
    for i in dic_nomes_e_idades.keys():
        if dic_nomes_e_idades[i]<=11:
            faixa_crianca.append(i)
        elif 12<=dic_nomes_e_idades[i]<=17:
            faixa_adolescente.append(i)
        elif 18<=dic_nomes_e_idades[i]<=59:
            faixa_adulto.append(i)
        else:
            faixa_idoso.append(i)
        dic_faixa_etaria['criança']=faixa_crianca
        dic_faixa_etaria['adolescente']=faixa_adolescente
        dic_faixa_etaria['adulto']=faixa_adulto
        dic_faixa_etaria['idoso']=faixa_idoso
    return dic_faixa_etaria
dicionario = {'Jão' : 35}
print(agrupa_por_idade(dicionario))