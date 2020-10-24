def remove_vogais(letras):
    lista=[]
    i=0
    while i < len(letras):
        if letras[i]!='a' and 'e' and 'i' and 'o' and 'u':
            lista.append(letras[i])
        elif letras[i]=='a' or 'e' or 'i' or 'o' or 'u' :
            i+=1
    print (lista)
               