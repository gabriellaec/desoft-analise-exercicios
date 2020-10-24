def aniversariantes_de_setembro(dicionario):
    dicionario2={}
   
   
    for i in dicionario.keys():
        for e in dicionario.values():
            if e[3]=='0'and e[4]=='9':
                dicionario2[i]=e
           
    return dicionario2
                