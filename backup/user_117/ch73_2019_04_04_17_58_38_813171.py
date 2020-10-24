def remove_vogais(letras):
    i=0
    while i<len(letras):
        if letras[i]== 'a' or letras[i] == 'e' or letras[i] == 'i' or letras[i] == 'o' or letras[i] == 'u':
            del letras[i]
    