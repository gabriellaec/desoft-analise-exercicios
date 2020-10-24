def inverte_dicionario(dicionario):
    dn={}
    ls=[]
    for n in dicionario.values():
        ls=[]
        if n not in dn:
            for f,m in dicionario.items():
                if n==m:
                    ls.append(f)
            dn[n]=ls        
    return dn
def agrupa_por_idade(dicionario):
    dc={'criança': [], 'adolescente': [], 'adulto': [], 'idoso': []}
    dn=inverte_dicionario(dicionario)
    ls1=[]
    ls2=[]
    ls3=[]
    ls4=[]
    for i,n in dn.items():
        if i<=11:
            ls1+=n
            dc['criança']=ls1
        elif i<=17 and i>=12:
            ls2+=n
            dc['adolescente']=ls2
        elif i>=18 and i<=59:
            ls3+=n
            dc['adulto']=ls3
        elif i>=60:
            ls4+=n
            dc['idoso']=ls4    
    return dc
            
            