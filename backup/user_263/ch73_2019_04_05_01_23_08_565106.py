def remove_vogais(string):
    letras=list(string)
    i=0
    consoantes=[]
    while i<len(letras):
        if letras[i]=='a' or letras[i]=='e' or letras[i]=='i' or letras[i]=='o' or letras[i]=='u':
            del letras[i]
        else: 
            i+=1
    if letras==[]:
        consoantes=[]
    else: 
        consoantes=''.join(letras)
    devolve=str(consoantes)
    return devolve
    