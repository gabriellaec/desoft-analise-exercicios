def conta_ocorrencias (palavras):
    dicio ={}
    for k in palavras:
        if k in dicio:
            dicio[k] +=1
        else:
            dicio[k] =1
    

def mais_frequente (dicio):
    outro_dic ={}
    for k in dicio:
        outro_dic[dicio.values()] = k
    max = 0
    for j in dicio:
        if j>max:
            max = j
    return outro_dic[max]