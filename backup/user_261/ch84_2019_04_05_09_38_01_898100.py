def inverte_dicionario(dicionario):
    d={}
    l=[]
    lrepetido=[]
    for nome, idade in dicionario.items():
        if idade not in d :
                 d[idade]= nome
        else:
                d[idade]= l.append(d[idade],nome)
      
    
    return d
            
