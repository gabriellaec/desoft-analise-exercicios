def aniversariantes_de_setembro (dicionario):
    dados={}
    i=0
    for p in dicionario:
        mes= dicionario.get(p)
        if mes[3] == '0' and  mes[4] == '9' :
                dicionario.append(dicionario[i])
                i+=1
        else:
            i+=1
    return dicionario
            
    