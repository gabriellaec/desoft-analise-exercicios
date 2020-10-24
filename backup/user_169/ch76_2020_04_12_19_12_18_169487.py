def aniversariantes_de_setembro(dicionario):
    dicionario2={}
   
   
    for i in dicionario:
        for e in dicionario.values():
            if e[4]=='0'and e[5]=='9':
                dicionario2[i]=e
           
    return dicionario2
                