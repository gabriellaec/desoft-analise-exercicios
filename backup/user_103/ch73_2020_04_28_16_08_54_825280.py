def remove_vogais(letras):
    letras.split()
    i=0
    while i < len(letras):
        if letras[i]=='a':
            del letras[i]
        if letras[i]=='e':
            del letras[i]
        if letras[i]=='i':
            del letras[i]
        if letras[i]=='o':
            del letras[i]
        if letras[i]=='u': 
            del letras[i]
        i+=1
    return letras