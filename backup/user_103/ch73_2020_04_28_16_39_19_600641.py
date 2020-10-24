def remove_vogais(letras):
    lista=[]
    i=0
    while i < len(letras):
        if letras[i]!='a' and letras[i]!='e' and letras[i]!='i' and letras[i]!='o' and letras[i]!='u':
            lista.append(letras[i])
            i+=1
        elif letras[i]=='a' or 'e' or 'i' or 'o' or 'u' :
            i+=1
    return ''.join(lista)
               