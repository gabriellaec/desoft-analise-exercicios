def aniversariantes_de_setembro (dicionario):
    dados={}
    i=0
    for p in dicionario:
        mes= dicionario.get(p)
        if mes[3] == '0' and  mes[4] == '9' :
                dados.append(dicionario[p])
                
        else:
            dados=dados
    return dados
            
    