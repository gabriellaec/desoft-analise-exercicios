def remove_vogais(string):
    resultado=[]
    i=0
    while i<len(string):
        if string[i]!='a' and string[i]!='e' and string[i]!='i' and string[i]!='o' and string[i]!='u':
            resultado.append(string[i])
        i+=1
    string_final=''.join(resultado)
    return string_final