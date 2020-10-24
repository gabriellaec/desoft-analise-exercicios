def remove_vogais(palavra):
    semvogais=[]
    i=0
    e=0
    palavrafinal=0
    consoantes=0
    while i<len(palavra):
        if palavra[i]!="a" and palavra[i]!="e" and palavra[i]!="i" and palavra[i]!="o" and palavra[i]!="u" :
            semvogais.append(palavra[i])
            consoantes+=1
        i+=1
    while e<len(semvogais):
        return semvogais[e]+semvogais[e+1]
        e+=1



    