def primeiras_ocorrencias(string):
    ocorrencias={}
    letras=[]
    index=[]
    for letra in range(len(string)):
        if letra not in letras:
            letras.append(letra)
            index.append(string[letra])
    for i in range(len(letras)):
        ocorrencias[letras[i]]=index[i]
    return ocorrencias
            
            
