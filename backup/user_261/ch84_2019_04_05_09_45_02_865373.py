def inverte_dicionario(dicionario):
    d={}
    l=[]
    lrepetido=[]
    for nome, idade in dicionario.items():
        if idade not in d :
                 d[idade]= nome
        else:
                l.append(d[idade])
                d[idade]=l.append(nome)
      
    
    return d
            
